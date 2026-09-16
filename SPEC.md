# Specification: ai-resources

Status: approved by the repository owner.

## Objective

Create a personal repository to collect, maintain, and reuse AI resources across projects: prompts, skills, agent definitions, rules, workflows, scripts, and documentation.

## Initial scope

- Organize resources by type, with a main README serving as an index.
- Document each resource's purpose, usage, compatibility, and requirements.
- Keep resources generic and explain the adaptations needed for each project.
- Add categories when there is content to justify them.

## Technology and commands

Markdown for documentation. Scripts will use the language appropriate to their function and document their dependencies and exact execution commands.

No application, package installation, build, or server is required to browse the repository.

Search commands from the root, with ripgrep installed:

```powershell
rg --files
rg -n "keyword" prompts skills agents rules workflows scripts docs
```

## Structure

```text
README.md           Index and usage guide
SPEC.md             Repository scope and conventions
prompts/            Reusable instructions for specific tasks
skills/             Skills, each in its own folder with its SKILL.md
agents/             Reusable agent definitions and configurations
rules/              Rules to adapt to each project's context
workflows/          Procedures that combine steps and resources
scripts/            Automations and executable utilities
docs/               Guides, references, and notes
```

`agents/` stores reusable resources. A future `AGENTS.md` at the root would contain instructions for working in this repository.

## Conventions

- Write documentation in English; preserve technical names and formats required by each tool.
- Use `kebab-case` for file and folder names, except for conventions such as README.md or SKILL.md.
- Organize by type first; add topic subfolders when they make content easier to find.
- Use relative links between resources.
- Record the source and license when copying or adapting third-party material.
- Specify compatible tools without assuming universal portability.

Example resource documentation:

```markdown
# Review changes

## Purpose
Identify errors and risks in a set of changes.

## Compatibility and requirements
An assistant with access to the project's diff.

## Usage
Replace {{context}} with the goal of the change and attach the diff.

## Content
Review the following diff considering {{context}}.
Prioritize behavioral errors and explain how to reproduce them.
```

Each tool's own formats take precedence over this example.

## Verification

- Check that the index and relative links point to existing resources.
- Check that each resource explains how to use it.
- For scripts, document and run a check appropriate to their behavior before considering them usable.
- No testing framework is needed for the initial documentation structure.

## Boundaries

- Always: keep resources understandable, reusable, and explicit about their requirements.
- Ask first: publish the repository or connect external services when no prior authorization exists.
- Never: store credentials, secrets, or private project data in examples.

## Acceptance criteria for the initial structure

- A main README explains the purpose and links to the seven proposed categories.
- Each category has a short guide on what to store and how to use it.
- The conventions allow resources to be added without depending on a specific project.
- No dependencies or automations are added without a concrete use case.

## Agreed decisions

Organization by resource type, documentation in English, and names in `kebab-case`, respecting each tool's own formats.
