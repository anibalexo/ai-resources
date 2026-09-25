# Plan a feature

## Purpose and requirements

Turn a feature request into a verifiable specification and technical plan, stopping before task breakdown and implementation. Follow the [documentation structure](../docs/documentation-structure.md). Requires the request and access to the target project's code, instructions, and documentation; no running application is required to begin.

This workflow is planning-only. Inspect the repository and create or update planning documents and their index links. Do not change application code, tests, runtime configuration, or dependencies; generate or apply migrations; create an execution task list; or perform deployment or external mutations. Describe proposed changes and validation commands in the plan without executing implementation steps. This scope applies when using the companion skills below, even if they also support implementation.

## Procedure

1. **Inspect and identify.** Read repository instructions, working tree status, relevant code, existing specifications, and plans. Preserve unrelated changes. Reuse or choose a stable kebab-case feature id. Respect established project paths; otherwise use `docs/features/<feature>/`.
2. **Clarify and specify.** Use [Specify feature](../skills/specify-feature/SKILL.md). Establish the problem, scope, expected behavior, constraints, acceptance criteria with stable ids, and unresolved decisions. Save or update `spec.md`. If the request bundles independent capabilities, establish their boundaries and dependency map before writing the affected specs.
3. **Prepare the technical plan.** Use [Plan implementation](../skills/plan-implementation/SKILL.md). Save or update `plan.md` with evidence from existing code, design alternatives and recommendation, affected files and symbols, model and data changes when relevant, dependency order, risks, and proposed verification. Link acceptance criteria instead of copying their definitions. In Django projects, reference [Django styleguide](../skills/django-styleguide/SKILL.md) for service/selector architecture, model constraints, and clean boundaries, and [Django safe migration](../skills/django-safe-migration/SKILL.md) when proposing schema or data changes to ensure zero-downtime compatibility. Include enough sequencing to explain the approach; stop before producing `tasks.md` or an execution checklist.
4. **Review and index.** Check that each acceptance criterion is addressed by the approach and a proposed verification. Confirm existing paths and symbols against the repository and identify new ones as proposals. Check document links and add the created documents to `docs/README.md` or the established index. Keep shared conventions linked from their existing source.
5. **Deliver and stop.** Return links to the specification and plan, the recommended approach, and any decisions still needed. Do not start implementation, generate tests, or create a usage guide for behavior that has not been implemented.

## Completion and unresolved decisions

The planning deliverable is ready when the scope, technical approach, impacts, risks, and verification are sufficiently defined. Record unresolved material decisions as a draft and explain which parts depend on them. Do not describe a plan as approved without actual approval or describe proposed checks as completed tests.

Ask focused questions when missing information changes the requirements or design. Continue independent inspection and document supported conclusions while waiting; do not treat silence as agreement. When access or context is missing, record the gap and the next investigation needed instead of inventing file paths or behavior.

If plans already exist, update them for the requested scope rather than creating duplicates. Preserve existing task lists and usage guides; identify inconsistencies for later resolution without expanding this workflow into implementation.

## Continue later

When the user requests implementation, use [Implement a feature](implement-feature.md). Revalidate the existing specification and plan against current code, resolve outstanding decisions, and continue with task breakdown. Reuse these documents rather than starting again.

## Example request

> Follow workflows/plan-feature.md to specify and plan order history. Save the documents in docs/features/order-history/ and stop after delivering the technical plan.
