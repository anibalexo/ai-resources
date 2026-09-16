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

- [Specify feature](specify-feature/SKILL.md): defines feature scope, expected behavior, and verifiable acceptance criteria in specifications using `docs/features/<feature>/`. Designed for Codex with repository access.
- [Optimize performance](optimize-performance/SKILL.md): diagnoses bottlenecks, distinguishes measurements from hypotheses, and verifies targeted optimizations while preserving behavior. Designed for Codex; uses the target project's runtime and diagnostic tools.
- [Generate tests](generate-tests/SKILL.md): derives meaningful cases from expected behavior, follows the project's testing conventions, and reports actual execution results. Designed for Codex; uses the target project's test framework and runtime.
- [Debug code](debug-code/SKILL.md): investigates root causes, separates reproduced defects from hypotheses, and verifies targeted fixes when requested. Designed for Codex; uses the target project's runtime and test tools when reproduction is available.
- [Plan implementation](plan-implementation/SKILL.md): creates technical implementation plans grounded in the existing code, including scope, design alternatives, affected files and model attributes, and validation. Designed for Codex with repository access.
- [Document features](document-features/SKILL.md): maintains usage guides, API references, and other affected documentation as features are added or changed, verifying claims against the implementation. Designed for Codex with repository access; uses existing documentation tooling when available.

## Install in Codex

Copy the complete folder of each desired skill into `$CODEX_HOME/skills`, or `~/.codex/skills` when `CODEX_HOME` is unset. Keep each `SKILL.md` inside its named folder. Installed copies must be updated separately when this repository changes.

Invoke a skill with `$specify-feature`, `$optimize-performance`, `$generate-tests`, `$debug-code`, `$plan-implementation`, or `$document-features` and describe the task and relevant code. Their descriptions also allow automatic selection for matching tasks. See each skill for its instructions and requirements.

The feature skills share the [documentation structure](../docs/documentation-structure.md). Use [Implement a feature](../workflows/implement-feature.md) to connect them into one procedure. Repository renames do not update installed copies. Review existing installations and local customizations when adopting these names.

For example: "Use $plan-implementation to plan order history for this project, including affected files, model changes, and validation."

To keep documentation aligned during development: "Implement order history and use $document-features to update the relevant documentation before finishing."

[Back to index](../README.md)
