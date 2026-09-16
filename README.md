# ai-resources

Reusable prompts, skills, and workflows for specifying, planning, implementing, testing, debugging, optimizing, and documenting software changes across projects. The skills are designed for Codex; prompts and workflow instructions can be adapted to other assistants with the required capabilities.

## Choose a resource

| I want to... | Resource |
| --- | --- |
| Specify and plan a feature without changing code | [Plan a feature](workflows/plan-feature.md) |
| Implement a feature from scratch or resume an existing plan | [Implement a feature](workflows/implement-feature.md) |
| Define requirements and acceptance criteria | [Specify feature](skills/specify-feature/SKILL.md) |
| Prepare a technical implementation plan | [Plan implementation](skills/plan-implementation/SKILL.md) |
| Create and run meaningful tests | [Generate tests](skills/generate-tests/SKILL.md) |
| Investigate bugs and verify requested fixes | [Debug code](skills/debug-code/SKILL.md) |
| Measure and optimize performance | [Optimize performance](skills/optimize-performance/SKILL.md) |
| Update documentation for implemented features | [Document features](skills/document-features/SKILL.md) |
| Copy a short prompt for a focused task | [Prompt catalog](prompts/README.md) |

## Quick start

Give your assistant access to the target project and the selected workflow. Use its actual accessible path when the workflow lives in a separate checkout of this repository. Keep linked resources accessible, or supply the relevant instructions directly; copying only a workflow file can break its relative links.

To create a specification and technical plan:

```text
Follow workflows/plan-feature.md to specify and plan order history in this
project. Save the documents in docs/features/order-history/ and stop after
reporting the technical plan and unresolved decisions. Do not implement code.
```

To implement the feature, including when a plan already exists:

```text
Follow workflows/implement-feature.md to implement order history in this
project. Reuse spec.md and plan.md in docs/features/order-history/ if present,
check them against the current code, then define tasks, implement, verify the
acceptance criteria, and update the documentation. Do not deploy.
```

The planning workflow stops at `spec.md` and `plan.md`. The implementation workflow also covers tasks, code changes, verification, and relevant usage documentation. Both follow the target project's instructions and requested scope.

## Resource types

- **Prompts** are instructions you copy into an assistant after replacing the documented placeholders and providing context.
- **Skills** provide reusable task guidance, with supporting resources when needed. Read their requirements and install them in the supported tool before invoking them as skills.
- **Workflows** coordinate stages and resources for a larger outcome. They are instructions for an assistant to follow, not programs that run on their own.

Choose a focused prompt or skill for a small task. Use a workflow when the work benefits from coordinated specification, planning, implementation, and verification.

## Installation

No dependencies are required to read this repository. For Codex skills, follow the [installation instructions](skills/README.md#install-in-codex), then invoke the desired skill, for example:

```text
Use $debug-code to investigate why submitting the checkout form twice creates
two orders. Reproduce the issue locally and explain the cause and proposed fix.
```

Keeping a skill in this repository does not install or activate it. Installed copies must be updated separately when repository resources change. Each resource documents its own requirements; execution may need the target project's runtime, test framework, or diagnostic tools.

## Documentation structure

Feature workflows use the following default layout in the **target project**, unless its instructions specify another convention:

```text
docs/
  README.md
  project.md
  features/
    <feature>/
      spec.md      # Requirements and acceptance criteria
      plan.md      # Technical design and implementation approach
      tasks.md     # Execution checklist and verification results
      usage.md     # How to use implemented behavior
  architecture/
    overview.md
    decisions/
  guides/
    development.md
```

Use a stable kebab-case feature id and create only the documents needed for the task. Shared information stays in project, architecture, and development guides. See the [documentation convention](docs/documentation-structure.md) for maintenance rules and instructions to adopt it in another project's `AGENTS.md`.

## Repository layout

| Folder | Contents | Availability |
| --- | --- | --- |
| [prompts](prompts/README.md) | Short instructions for focused tasks | Resources available |
| [skills](skills/README.md) | Reusable task guidance for Codex | Resources available |
| [workflows](workflows/README.md) | Planning and implementation procedures | Resources available |
| [docs](docs/README.md) | Guides and conventions for reusing these resources | Resources available |
| [agents](agents/README.md) | Agent definitions and configurations | No resources added yet |
| [rules](rules/README.md) | Reusable project and assistant rules | No resources added yet |
| [scripts](scripts/README.md) | Executable automations | No resources added yet |

Search from the repository root with ripgrep:

```powershell
rg --files
rg -n "keyword" prompts skills agents rules workflows scripts docs
```

## Contributing

- Save resources in the appropriate category using descriptive kebab-case names, preserving tool conventions such as `SKILL.md`.
- Explain purpose, compatibility, requirements, usage, and expected output.
- Document placeholders such as `{{context}}` and any project-specific adaptations.
- Write documentation in English and keep examples free of credentials and private data.
- Record the source and license when adapting third-party content.
- Add the resource to its category's catalog and verify relative links.
- Group supporting files with their resource, following the target tool's format. Add scripts or other dependencies only when they serve a concrete need, and document and verify their use.

See [SPEC.md](SPEC.md) for the repository's scope and maintenance criteria.
