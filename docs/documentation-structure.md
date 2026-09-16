# Project documentation structure

Use this convention when organizing documentation for a new project or when explicitly adopting it in an existing one. Existing project instructions and explicit user paths take precedence. The procedure that uses these paths is [Implement a feature](../workflows/implement-feature.md).

## Layout

```text
docs/
  README.md
  project.md
  features/
    order-history/
      spec.md
      plan.md
      tasks.md
      usage.md
  architecture/
    overview.md
    decisions/
  guides/
    development.md
```

`order-history` is an example feature id, not a folder every project must create. Create only documents that contain useful information; small changes may need only a concise existing document update.

| Path | Responsibility |
| --- | --- |
| `docs/README.md` | Index of existing documentation and feature documents |
| `docs/project.md` | Shared project purpose, scope, stack, and conventions |
| `docs/features/<feature>/spec.md` | Required behavior, boundaries, and acceptance criteria |
| `docs/features/<feature>/plan.md` | Technical design, affected files and models, risks, and implementation order |
| `docs/features/<feature>/tasks.md` | Execution checklist, dependencies, acceptance ids, and verification results |
| `docs/features/<feature>/usage.md` | How to use implemented behavior, examples, and limitations |
| `docs/architecture/overview.md` | Architecture shared across features |
| `docs/architecture/decisions/` | Significant architectural decisions and their rationale |
| `docs/guides/development.md` | Environment setup and actual development, test, and build commands |

## Maintenance rules

- Use a stable kebab-case feature id across all its documents. Update existing documents for the same capability rather than creating a new folder for every iteration.
- Give acceptance criteria stable ids such as `AC-01`; reference them from tasks and verification results.
- Keep requirements, technical decisions, execution status, and user instructions in their respective documents. Link shared facts instead of copying them.
- Record status honestly: a proposed plan is not approved, an implemented task is not necessarily verified, and neither means deployed.
- Update the index with relative links to documents that actually exist. Keep the root README and tool entry points such as AGENTS.md in their required locations.
- For a multi-capability initiative, use `docs/features/<initiative>/capability-map.md` as an index of capability ids, dependencies, and their feature folders. Skip this for one cohesive feature.

## Adopt in another project

Record this convention in the target project's instructions, normally `AGENTS.md`, so it applies consistently. For example:

```markdown
## Documentation

Keep generated feature documentation in docs/features/<feature>/ using a
stable kebab-case id: spec.md for requirements, plan.md for technical design,
tasks.md for execution and verification, and usage.md for implemented usage.
Create only needed documents and index them in docs/README.md.
Keep shared context in docs/project.md, shared architecture in
docs/architecture/, and development setup in docs/guides/development.md.
Update existing documents rather than duplicating them.
```

Install the desired [skills](../skills/README.md) separately. Copying this guide or a skill into a repository does not automatically install or activate it.

For an existing project, first inventory its canonical documents and any tooling that depends on their paths. Migrate only when requested, then update links and tool configuration in the same change. Do not leave two editable sources of truth.

In this resource repository, this guide defines the reusable convention; it does not move the existing root `SPEC.md` or create example application folders. The workflow explains the sequence, and each skill carries its own default paths so installed copies remain self-contained.
