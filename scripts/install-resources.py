#!/usr/bin/env python3
"""Install local resources. Python 3.10+, no third-party dependencies."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tempfile

SOURCE = Path(__file__).resolve().parent.parent
MANIFEST = Path('.agents/ai-resources-manifest.json')
NAME = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')
LINK = re.compile(r'\[([^\]\n]+)\]\(([^)\s]+)\)')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_path(root, relative):
    relative = Path(relative)
    if relative.is_absolute() or '..' in relative.parts:
        raise ValueError(f'Unsafe destination: {relative}')
    candidate = root / relative
    for part in [candidate, *candidate.parents]:
        if part.exists() or part.is_symlink():
            info = part.lstat()
            if part.is_symlink() or getattr(info, 'st_file_attributes', 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT:
                raise ValueError(f'Symbolic links and junctions are not supported: {part}')
    for parent in candidate.parents:
        if parent.exists() and not parent.is_dir():
            raise ValueError(f'Destination parent is not a directory: {parent}')
    if not candidate.resolve().is_relative_to(root.resolve()):
        raise ValueError(f'Destination leaves project: {relative}')
    return candidate


def revision(source):
    try:
        commit = subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], stderr=subprocess.DEVNULL, text=True).strip()
        dirty = bool(subprocess.check_output(['git', '-C', str(source), 'status', '--porcelain'], stderr=subprocess.DEVNULL, text=True).strip())
        return {'commit': commit, 'dirty': dirty}
    except (OSError, subprocess.CalledProcessError):
        return {'commit': None, 'dirty': None}


def build_files(source, skills, workflows):
    available_skills = {p.parent.name for p in (source / 'skills').glob('*/SKILL.md')}
    available_workflows = {p.stem for p in (source / 'workflows').glob('*.md') if p.name != 'README.md'}
    if not skills and not workflows:
        skills, workflows = available_skills.copy(), available_workflows.copy()
    else:
        skills, workflows = set(skills), set(workflows)
    for chosen, available in [(skills, available_skills), (workflows, available_workflows)]:
        for name in chosen:
            if not NAME.fullmatch(name) or name not in available:
                raise ValueError(f'Unknown resource: {name}')
    for name in workflows:
        text = (source / 'workflows' / f'{name}.md').read_text(encoding='utf-8')
        skills.update(re.findall(r'\.\./skills/([a-z0-9-]+)/SKILL\.md', text))
    if not skills <= available_skills:
        raise ValueError('A workflow refers to a missing skill.')
    mapping = {}
    for name in sorted(skills):
        directory = source / 'skills' / name
        for file in directory.rglob('*'):
            if file.is_symlink() or getattr(file.lstat(), 'st_file_attributes', 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT:
                raise ValueError(f'Symbolic source paths are not supported: {file}')
            if file.is_file():
                mapping[file.resolve()] = Path('.agents/skills') / name / file.relative_to(directory)
    for name in sorted(workflows):
        mapping[(source / 'workflows' / f'{name}.md').resolve()] = Path('.agents/workflows') / f'{name}.md'
    if workflows:
        mapping[(source / 'docs/documentation-structure.md').resolve()] = Path('.agents/docs/documentation-structure.md')
    # Installed catalogs contain only selected resources, avoiding dangling links.
    mapping[(source / 'skills/README.md').resolve()] = Path('.agents/skills/ai-resources.md')
    files, omitted = {}, []
    for original, target in mapping.items():
        if original == (source / 'skills/README.md').resolve():
            continue
        data = original.read_bytes()
        if original.suffix == '.md':
            def rewrite(match):
                label, href = match.groups()
                if '://' in href or href.startswith(('#', 'mailto:')):
                    return match[0]
                path, separator, anchor = href.partition('#')
                linked = (original.parent / path).resolve()
                if not linked.exists():
                    raise ValueError(f'Missing source link: {original}: {href}')
                if linked not in mapping:
                    omitted.append(f'{target.as_posix()}: {href}')
                    return f'{label} (not included in this installation)'
                relative = os.path.relpath(mapping[linked], target.parent).replace(os.sep, '/')
                return f'[{label}]({relative}{separator}{anchor})'
            text = LINK.sub(rewrite, data.decode('utf-8-sig'))
            text = text.replace('workflows/plan-feature.md', '.agents/workflows/plan-feature.md') if target.name == 'plan-feature.md' else text
            files[target.as_posix()] = text.encode('utf-8')
        else:
            files[target.as_posix()] = data
    catalog = '# Installed AI skills\n\n' + ''.join(f'- [{name}]({name}/SKILL.md)\n' for name in sorted(skills))
    files['.agents/skills/ai-resources.md'] = catalog.encode()
    proposal = '# Suggested project instructions\n\nReview and merge the following block into the project AGENTS.md if appropriate.\nExisting project instructions take precedence. This file is not an automatically loaded AGENTS.md.\n\n```markdown\n## AI resources\n\n'
    for name in sorted(workflows):
        proposal += f'- Use `.agents/workflows/{name}.md` when that workflow matches the requested task.\n'
    proposal += 'Keep feature documents in `docs/features/<feature>/`: spec.md for requirements,\nplan.md for technical design, tasks.md for execution, and usage.md for implemented\nbehavior. Create only needed documents and link them from docs/README.md.\nRespect planning-only requests and preserve existing project conventions.\n```\n'
    files['.agents/ai-resources-instructions.md'] = proposal.encode()
    return files, omitted


def install(source, target, skills=(), workflows=(), update=False, dry_run=False):
    source = Path(source).resolve()
    raw_target = Path(target).absolute()
    if not raw_target.is_dir():
        raise ValueError('Target must be an existing project directory.')
    # Reject symlinked parent directories before resolving away that evidence.
    safe_path(raw_target, Path('.'))
    target = raw_target.resolve()
    if target == source or target.is_relative_to(source) or source.is_relative_to(target):
        raise ValueError('Target and source repositories must not contain one another.')
    manifest_path = safe_path(target, MANIFEST)
    previous = {'schema_version': 1, 'files': {}}
    if manifest_path.exists():
        previous = json.loads(manifest_path.read_text(encoding='utf-8'))
        if previous.get('schema_version') != 1 or not isinstance(previous.get('files'), dict):
            raise ValueError('Unsupported or invalid installation manifest.')
    # Preserve the catalog and instructions for resources already managed here.
    if skills or workflows:
        skills, workflows = set(skills), set(workflows)
        for relative in previous['files']:
            match = re.fullmatch(r'\.agents/skills/([a-z0-9-]+)/SKILL\.md', relative)
            if match and (source / 'skills' / match[1] / 'SKILL.md').is_file():
                skills.add(match[1])
            match = re.fullmatch(r'\.agents/workflows/([a-z0-9-]+)\.md', relative)
            if match and (source / 'workflows' / f'{match[1]}.md').is_file():
                workflows.add(match[1])
    files, omitted = build_files(source, skills, workflows)
    actions, conflicts = [], []
    for relative, data in files.items():
        path = safe_path(target, relative)
        if path.exists():
            if not path.is_file():
                conflicts.append(f'{relative}: destination is not a file')
                continue
            current = digest(path.read_bytes())
            if current == digest(data):
                actions.append(('UNCHANGED', relative))
                continue
            record = previous['files'].get(relative)
            if not update or not isinstance(record, dict) or current != record.get('sha256'):
                conflicts.append(f'{relative}: existing content differs; only unchanged managed files can be replaced with --update')
                continue
            actions.append(('UPDATE', relative))
        else:
            actions.append(('CREATE', relative))
    for action, relative in actions:
        print(f'{action:9} {relative}')
    for reference in omitted:
        print(f'OPTIONAL LINK omitted: {reference}')
    if conflicts:
        raise ValueError('No files written. Resolve conflicts first:\n' + '\n'.join(conflicts))
    print(f'MANIFEST  {MANIFEST.as_posix()}')
    if dry_run:
        print('Preview only; no files written.')
        return
    source_info = {'path': str(source), **revision(source)}
    records = dict(previous['files'])
    for action, relative in actions:
        data = files[relative]
        path = safe_path(target, relative)
        if action != 'UNCHANGED':
            path.parent.mkdir(parents=True, exist_ok=True)
            atomic_write(path, data)
        records[relative] = {'sha256': digest(data), 'source': source_info}
    manifest = {'schema_version': 1, 'updated_at': datetime.now(timezone.utc).isoformat(), 'files': records}
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    atomic_write(manifest_path, (json.dumps(manifest, indent=2) + '\n').encode())
    print('Installed. Review .agents/ai-resources-instructions.md; AGENTS.md was not edited.')


def atomic_write(path, data):
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(data)
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', type=Path, required=True)
    parser.add_argument('--skill', action='append', default=[])
    parser.add_argument('--workflow', action='append', default=[])
    parser.add_argument('--update', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        install(SOURCE, args.target, args.skill, args.workflow, args.update, args.dry_run)
    except (OSError, ValueError) as exc:
        print(f'Installation failed: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
