#!/usr/bin/env python3
"""Validate this repository's Markdown resources using Python 3.10+ only."""

import argparse
from collections import Counter
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
INLINE = re.compile(r"!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s)]+)(?:\s+[\"'][^\n]*?[\"'])?\s*\)")
DEFINITION = re.compile(r"^ {0,3}\[([^\]]+)\]:\s*(<[^>]+>|\S+)", re.M)
REFERENCE = re.compile(r"!?\[([^\]\n]+)\]\[([^\]\n]*)\]")
SKIP = {".git", ".venv", "venv", "node_modules", "__pycache__"}


def prose(text):
    """Exclude fenced examples from link and heading checks."""
    lines, fence = [], None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            lines.append("")
        else:
            lines.append(line if fence is None else "")
    return "\n".join(lines)


def anchors(text):
    result, counts = set(), Counter()
    for heading in re.findall(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", prose(text), re.M):
        heading = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", heading)
        heading = re.sub(r"<[^>]+>", "", heading)
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        number = counts[slug]
        counts[slug] += 1
        result.add(slug if number == 0 else f"{slug}-{number}")
    result.update(re.findall(r'(?:id|name)=[\"\']([^\"\']+)[\"\']', prose(text)))
    return result


def metadata(text):
    """Read required plain/quoted/block scalars, not arbitrary YAML."""
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
    if not match:
        raise ValueError("missing YAML frontmatter")
    fields = {}
    lines = match[1].splitlines()
    for i, line in enumerate(lines):
        item = re.match(r"^([a-z][a-z0-9_-]*):\s*(.*)$", line)
        if not item:
            continue
        key, value = item.groups()
        if key in fields:
            raise ValueError(f"duplicate metadata key: {key}")
        if value in (">", "|", ">-", "|-"):
            block = []
            for following in lines[i + 1:]:
                if following and not following.startswith((" ", "\t")):
                    break
                block.append(following.strip())
            value = " ".join(block)
        elif value.startswith(('"', "'")):
            if len(value) < 2 or value[-1] != value[0]:
                raise ValueError(f"unclosed scalar: {key}")
            value = value[1:-1]
        if key in ("name", "description") and (not value.strip() or value.startswith(("[", "{"))):
            raise ValueError(f"{key} must be a nonempty text scalar")
        fields[key] = value
    for key in ("name", "description"):
        if key not in fields:
            raise ValueError(f"missing metadata: {key}")
    return fields


def validate(root):
    root = Path(root).resolve()
    errors = []
    files = sorted(p for p in root.rglob("*.md") if not any(x in SKIP for x in p.relative_to(root).parts))
    if not files:
        return ["No Markdown resources found."]
    skills = {p.parent.name for p in files if p.name == "SKILL.md"}
    seen = set()
    for file in files:
        rel = file.relative_to(root)
        if file.is_symlink() or not file.resolve().is_relative_to(root):
            errors.append(f"{rel}: symbolic or external path is not supported")
            continue
        try:
            text = file.read_text(encoding="utf-8-sig")
        except (UnicodeError, OSError) as exc:
            errors.append(f"{rel}: {exc}")
            continue
        if file.name not in {"README.md", "SPEC.md", "SKILL.md", "AGENTS.md"} and not NAME.fullmatch(file.stem):
            errors.append(f"{rel}: use a kebab-case filename")
        if file.name == "SKILL.md":
            try:
                fields = metadata(text)
                name = fields["name"]
                if not NAME.fullmatch(name) or len(name) > 64 or name != file.parent.name:
                    errors.append(f"{rel}: name must match its kebab-case folder (max 64 characters)")
                if name in seen:
                    errors.append(f"{rel}: duplicate skill name {name}")
                seen.add(name)
                if len(fields["description"]) > 1024:
                    errors.append(f"{rel}: description exceeds 1024 characters")
            except ValueError as exc:
                errors.append(f"{rel}: {exc}")
        if "[TODO:" in text:
            errors.append(f"{rel}: unfinished scaffold placeholder")
        for invocation in re.findall(r"\$([a-z][a-z0-9]*(?:-[a-z0-9]+)+)", text):
            if invocation not in skills:
                errors.append(f"{rel}: unknown local skill invocation ${invocation}")
        clean = prose(text)
        definitions = {k.casefold(): v for k, v in DEFINITION.findall(clean)}
        targets = [m[1] for m in INLINE.finditer(clean)] + list(definitions.values())
        for label, reference in REFERENCE.findall(clean):
            if (reference or label).casefold() not in definitions:
                errors.append(f"{rel}: undefined reference link [{reference or label}]")
        for target in targets:
            target = target.strip("<>")
            parts = urlsplit(target)
            if parts.scheme or parts.netloc:
                continue
            path = unquote(parts.path)
            resolved = (file.parent / path).resolve() if path else file.resolve()
            if not resolved.is_relative_to(root):
                errors.append(f"{rel}: link leaves repository: {target}")
            elif not resolved.exists():
                errors.append(f"{rel}: missing link target: {target}")
            elif parts.fragment and resolved.suffix.lower() == ".md":
                if unquote(parts.fragment) not in anchors(resolved.read_text(encoding="utf-8-sig")):
                    errors.append(f"{rel}: missing heading anchor: {target}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    if not args.root.is_dir():
        parser.error("--root must be an existing directory")
    errors = validate(args.root)
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        print(f"Validation failed: {len(errors)} issue(s).", file=sys.stderr)
        return 1
    print("Resource validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
