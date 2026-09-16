# Skills

Reusable capabilities for assistants, with instructions and, when needed, scripts, references, or examples.

## Organization

Save each skill in a folder named in `kebab-case` with a `SKILL.md` file. Preserve the structure and metadata required by the target tool.

## What to document

- Purpose and conditions that trigger its use.
- Compatible tool and dependencies.
- Steps to install it or incorporate it into a project.
- Instructions, supporting resources, and a usage example.
- Source and license if it comes from a third party.

## Usage

Review `SKILL.md` and its supporting files before installing the skill. Follow the instructions specific to its tool and verify that it works using the documented example.

Saving a skill here does not automatically install or activate it.

## Catalog

- [Improve performance](improve-performance/SKILL.md): diagnoses bottlenecks, distinguishes measurements from hypotheses, and verifies targeted optimizations while preserving behavior. Designed for Codex; uses the target project's runtime and diagnostic tools.
- [Generate tests](generate-tests/SKILL.md): derives meaningful cases from expected behavior, follows the project's testing conventions, and reports actual execution results. Designed for Codex; uses the target project's test framework and runtime.
- [Find bugs](find-bugs/SKILL.md): investigates root causes, separates reproduced defects from hypotheses, and verifies targeted fixes when requested. Designed for Codex; uses the target project's runtime and test tools when reproduction is available.

## Install in Codex

Copy the complete folder of each desired skill into `$CODEX_HOME/skills`, or `~/.codex/skills` when `CODEX_HOME` is unset. Keep each `SKILL.md` inside its named folder. Installed copies must be updated separately when this repository changes.

Invoke a skill with `$improve-performance`, `$generate-tests`, or `$find-bugs` and describe the task and relevant code. Their descriptions also allow automatic selection for matching tasks. See each skill for a complete example and requirements.

[Back to index](../README.md)
