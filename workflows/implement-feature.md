# Implement a feature

## Purpose and requirements

Take a feature from requirements to verified implementation and usage documentation using the [documentation structure](../docs/documentation-structure.md). Requires the feature request, access to the target repository, and its development tools for execution. Companion skills support the stages; if unavailable, follow the described procedure directly.

Follow the target project's instructions and authorization. A request for a specification or plan does not authorize implementation. When implementation is already authorized, continue once material decisions are resolved without adding redundant approval steps. This procedure does not authorize publishing or deployment.

## Procedure

1. **Identify the feature.** Inspect the existing code, documentation, and pending changes. Reuse or choose a stable kebab-case id such as `order-history`. Locate its existing documents before creating new ones. Decompose only when independently testable capabilities justify separate specs.
2. **Specify the behavior.** Use [Specify feature](../skills/specify-feature/SKILL.md). Save requirements and acceptance ids in `docs/features/<feature>/spec.md`. Resolve questions that block dependent work; keep unresolved proposals clearly marked.
3. **Plan the implementation.** Use [Plan implementation](../skills/plan-implementation/SKILL.md). Save technical decisions, affected files and models, dependencies, risks, and checks in the same folder's `plan.md`. Link acceptance criteria from the spec.
4. **Define tasks.** Save focused tasks in that folder's `tasks.md`, each with acceptance ids, files, dependencies, and verification. Confirm every acceptance criterion is covered. Keep this separate from the design rationale in the plan.
5. **Implement and verify.** Work in dependency order within scope. Use [Implement code](../skills/implement-code/SKILL.md) to apply early returns, readability, and maintainable structure. Use [Generate tests](../skills/generate-tests/SKILL.md) for relevant behavioral coverage and [Debug code](../skills/debug-code/SKILL.md) when failures need investigation. Use [Optimize performance](../skills/optimize-performance/SKILL.md) only when a performance objective requires it. Record actual verification results; do not mark failed or unexecuted checks as passed.
6. **Document the result.** Use [Document features](../skills/document-features/SKILL.md). Update `usage.md` when a dedicated guide is useful and update affected shared documentation. Link created documents from `docs/README.md`. Reconcile any changed requirements or technical decisions with the spec and plan.

## Completion and recovery

For a complete feature, each acceptance criterion must be implemented and verified, task outcomes must reflect actual results, and relevant documentation must match the behavior. Report any unmet criterion or unavailable check instead of claiming completion. For a planning-only request, deliver the requested documents and unresolved decisions without implementing.

If checks fail, investigate the cause and revise the relevant change; preserve unrelated work. If requirements change, update the affected spec, plan, and tasks before continuing. If tooling or access blocks verification, record the command, limitation, and next action. Resume from the existing documents and actual code state rather than rebuilding the plan from scratch.

## Example request

> Implement order history using this workflow. Keep its documentation in docs/features/order-history/, verify the acceptance criteria, and update the documentation index. Do not deploy.
