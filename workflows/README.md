# Workflows

Reusable procedures that combine prompts, skills, agents, rules, or scripts to complete a task.

## Organization

Save each procedure in a Markdown file. If it includes an executable configuration, group it with its guide in its own folder.

## What to document

- Objective, requirements, and inputs.
- Steps in order, with relative links to the resources used.
- Decisions, human reviews, and external actions required by the process.
- Expected output and how to check it.
- How to continue or recover work if a step fails.

## Usage

Prepare the requirements and follow the steps in order. Check the result of each stage before moving on. If automation is available, review its configuration and effects before running it.

## Catalog

- [Plan a feature](plan-feature.md): produces the specification and technical plan under `docs/features/<feature>/`, stopping before task breakdown or code changes.
- [Implement a feature](implement-feature.md): connects specification, technical planning, tasks, implementation, verification, and documentation under `docs/features/<feature>/`.

[Back to index](../README.md)
