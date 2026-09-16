# Scripts

Automations and executable utilities to support the use of AI across projects.

## Organization

Use descriptive names in `kebab-case` and the appropriate language extension. Group scripts with dependencies, configurations, or supporting files in their own folder.

## What to document

- Purpose, required operating system, and interpreter version.
- Dependencies and exact installation and execution commands.
- Working directory, arguments, and environment variables.
- Inputs, outputs, and files or services it modifies.
- An example with fictional data and a way to check the result.

## Usage

Read the script's guide, prepare its requirements, and run it with your project's arguments. Test scripts that modify files on sample data before using them with working data.

Each script manages its own requirements; the repository has no global dependencies. Keep credentials out of code and examples.

## Catalog

- [Install resources](install-resources.ps1): Windows PowerShell entry point for installing selected skills and workflows into an existing project. Uses the [Python installation engine](install-resources.py).
- [Validate resources](validate-resources.py): checks local Markdown resources without third-party packages.

## Requirements

Python 3.10+ is required. The PowerShell wrapper supports Windows PowerShell 5.1+ and PowerShell 7. No package installation or network access is required by these scripts. Commands below run from this repository's root; the scripts also resolve their source location when called from elsewhere.

## Install or update resources

Start with a preview against an existing target project:

```powershell
.\scripts\install-resources.ps1 -TargetPath 'C:\Projects\My App' -WhatIf
```

Install everything by omitting resource selections, or choose workflows and skills:

```powershell
.\scripts\install-resources.ps1 -TargetPath 'C:\Projects\My App' -Workflows plan-feature
.\scripts\install-resources.ps1 -TargetPath 'C:\Projects\My App' -Skills debug-code,generate-tests -Update
```

Workflow selections automatically include their linked skills. Already managed resources remain in the installation catalog when adding more selections. Updates require `-Update` if generated content differs. Use `-Python 'C:\Path\To\python.exe'` if Python is not on PATH.

If the host blocks PowerShell scripts, use the Python entry point; the installer does not change execution policy:

```text
python scripts/install-resources.py --target "C:\Projects\My App" --workflow plan-feature --dry-run
python scripts/install-resources.py --target "C:\Projects\My App" --workflow plan-feature
python scripts/install-resources.py --target "C:\Projects\My App" --skill debug-code --update
```

Repeat `--skill` or `--workflow` to select multiple resources in Python. The engine also runs on Linux and macOS with native target paths.

### Installed output and conflict handling

```text
.agents/
  skills/<skill>/SKILL.md
  skills/ai-resources.md
  workflows/<workflow>.md
  docs/documentation-structure.md
  ai-resources-instructions.md
  ai-resources-manifest.json
```

The documentation guide is included when workflows are selected. Markdown links are adapted to installed locations. Optional links to resources outside the selection become labeled text, and the installer reports each omission. These scripts support the repository's simple inline Markdown link format for installation.

`ai-resources-instructions.md` proposes a block to review and merge into the project's `AGENTS.md`; the installer never edits `AGENTS.md`, application code, or project documentation. Instructions in that proposal use `docs/features/<feature>/` for future feature artifacts.

The manifest records source path, Git revision and dirty status when available, and the SHA-256 hash and provenance of each installed file. A dirty source means the commit alone does not fully identify the input; file hashes identify the installed content. Review and commit this repository before distributing a reproducible version.

- Preview performs no writes and reports conflicts as failures.
- Identical existing content is reused; a successful install records it as managed.
- Different unmanaged content or locally edited managed content aborts the entire preflight before writes.
- An explicit update replaces only managed files whose current hashes still match their recorded installation. There is no force-overwrite option.
- Selected resources are additive. The installer does not delete resources that disappear upstream or rename old installations automatically. Review obsolete files manually.
- Targets must exist and must not contain or be contained by the source repository. Symbolic links and junctions in destination paths are rejected.

Conflicts require manual comparison and reconciliation. A filesystem error after preflight can leave a partial installation; writes are atomic per file, not transactional across the project. Fix the underlying error and preview again before retrying.

## Validate resources

```text
python scripts/validate-resources.py
python scripts/validate-resources.py --root "C:\Projects\My App\.agents"
```

The validator returns zero on success and one for validation failures. It checks required skill metadata and matching folder names, duplicate skill names, Markdown filenames, unfinished scaffold markers, local links and heading fragments, explicit reference links, and unknown local skill invocations. It ignores fenced examples when checking links.

This is a repository-focused validator, not a full YAML or CommonMark implementation. Metadata supports plain, quoted, and folded required scalars. Markdown link checking supports ordinary inline links and explicit reference definitions, plus ATX heading anchors and HTML ids. External URLs are not fetched; bare paths inside code blocks are not validated. It does not prove that skill behavior is correct or replace the official skill validator.

## Verification and CI

```text
python -m unittest discover -s scripts/tests -v
```

Tests use temporary sample projects and cover preview, dependency selection, conflict preservation, controlled updates, incremental selection, provenance hashes, links, validator failures, and path restrictions. Symlink tests can be skipped when the host lacks permission to create them. The PowerShell entry-point test runs on Windows; a local execution-policy block is reported as a skip, but is a failure in CI.

[GitHub Actions](../.github/workflows/validate.yml) runs validation and the tests on Linux and Windows for pushes and pull requests, and supports manual dispatch. No deployment step is included. A local pass does not establish that the remote CI run has completed.

[Back to index](../README.md)
