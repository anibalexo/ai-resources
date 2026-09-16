---
name: specify-feature
description: Create or update feature specifications with scope, expected behavior, constraints, and verifiable acceptance criteria. Use before technical planning when requirements are unclear or a feature needs a written contract. Decompose independently testable capabilities when necessary. Does not produce implementation plans, task lists, or code.
---

# Specify feature

Define what must be built and how completion will be verified. Keep specifications aligned with decisions throughout development. This skill produces specifications and, when needed, a capability map; technical planning and implementation belong to later workflow stages. Do not generate plans, task lists, code, tests, or migrations as part of this skill.

## Establish scope

Read repository instructions, relevant code, existing documentation, and working tree status. Preserve unrelated work. Identify the objective, users, current and expected behavior, constraints, and exclusions. Distinguish verified facts, assumptions, and unresolved decisions. Ask focused questions when an answer materially changes requirements; continue independent investigation while answers are pending.

If a request bundles independently testable capabilities, propose a small capability map with stable kebab-case ids, responsibilities, dependencies, and build order. Resolve material boundary decisions before writing dependent specifications. Store the map at `docs/features/<initiative>/capability-map.md` and link each capability's own feature folder. Do not split a single cohesive capability merely to create a hierarchy.

## Specify

Respect explicit project paths. Otherwise use `docs/features/<feature>/spec.md`, reusing an existing stable kebab-case feature id. Link it from `docs/README.md`. Create only needed documents; do not migrate existing files unless requested.

For a new specification without an established project template, start from [assets/spec-template.md](assets/spec-template.md). Adapt it to the requested scope and the project's documentation language; replace every `{{placeholder}}`, remove authoring comments and inapplicable optional sections, and resolve links relative to the output document. Preserve the structure of existing specifications when updating them rather than overwriting them with the template.

Include the objective, scope, observable behavior, relevant interfaces and business rules, constraints, acceptance criteria, assumptions, and open questions. Give acceptance criteria stable ids such as `AC-01` so tasks and tests can refer to them. Include relevant failure cases and permissions. Propose measurable targets when useful, but do not invent agreed business rules or performance requirements.

Reference shared stack, commands, structure, style, and testing conventions in `docs/project.md` or `docs/guides/development.md` when available. Record only feature-specific differences in the spec. Verify commands against the repository instead of copying generic examples. Keep architecture-wide material in the existing architecture documentation, defaulting to `docs/architecture/overview.md` and `docs/architecture/decisions/` when needed.

## Review and maintain

Record status and unresolved decisions accurately. Do not label a specification approved without actual approval. For unresolved material requirements, deliver a useful draft identifying which decisions remain open rather than inventing answers. Do not treat silence as agreement.

Before handing off, check that acceptance criteria are observable, consistent with the scope, and sufficiently concrete to guide later design and testing. Confirm that any existing paths or contracts cited were inspected and that proposals are labeled as proposals. Check document links and update the documentation index.

When requirements change, update the affected specification before downstream implementation of the new behavior. Preserve still-valid decisions and acceptance ids; identify downstream plans, tasks, or guides that may need revision without rewriting them within this skill. Do not mark behavior implemented, tested, or deployed based on a specification alone.

## Deliverable and handoff

Return links to the specification and any capability map, the defined scope, acceptance criteria, and unresolved decisions. Stop this skill at the specification deliverable. A calling workflow may then proceed to technical planning or implementation when authorized; this skill does not require an additional approval merely to hand off.

For the next stage, use `plan-implementation` when available or follow the target project's planning procedure. Keep the specification versioned alongside the project and reference its acceptance ids from later plans, tasks, and verification.

## Requirements and example

Designed for Codex with repository access. No companion skills or extra packages are required to produce the specification.

Example: "Use $specify-feature to define order history in docs/features/order-history/spec.md, including scope, permissions, and verifiable acceptance criteria. Identify unresolved requirements."

This skill adapts the specification stage of the user's existing local `spec-driven-development` skill to the repository's documentation convention. It is maintained separately from that installed source and leaves coordination of later stages to workflows.
