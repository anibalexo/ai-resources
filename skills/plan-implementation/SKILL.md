---
name: plan-implementation
description: Create or update technical implementation plans with requirements, scope, design alternatives, decision questions, and concrete impacts on files, functions, and model attributes. Use when asked to plan a feature, analyze its implementation, or define changes before coding. Not for focused fixes that do not require planning.
---

# Plan implementation

Turn the requirement into a verifiable plan grounded in the current code. Write in the user's language; preserve symbol names in the project's language. The result should explain what changes, why, where, and how it will be verified.

## Scope of work

If the user requests only a plan, inspect the project and create or update documentation; do not implement code, generate migrations, or run processes with external side effects. If implementation is also authorized, complete the plan first and continue within that authorization once the necessary decisions are resolved. Do not add approval gates for every phase or ask again about decisions already made.

## 1. Understand the requirement and current state

- Read repository instructions, relevant documentation, and `git status`. Preserve existing changes.
- Describe the problem, actors, current behavior, and expected behavior with a concrete example. Separate requested work from optional improvements.
- Define scope, exclusions, business rules, constraints, and observable acceptance criteria. Do not invent performance limits, volumes, or business rules; identify them as proposals or questions.
- Search for definitions, consumers, and tests. Trace the flow from web/API/task entry points through services, queries, persistence, and outputs. Inspect indirect consumers, reports, and exports when relevant.
- Cite existing paths and symbols that support the diagnosis. Distinguish verified facts, inferences, assumptions, and proposals; a new path is a proposal, not evidence of existing code.
- Read previous plans as context and compare them with the implementation. Do not present documented work as completed work.

## 2. Propose alternatives and ask about implementation decisions

When a decision has material consequences, compare the simplest solution that meets the requirement with viable alternatives. Do not invent alternatives for trivial changes.

Evaluate as appropriate:

- Scalability: expected volume, queries, justified indexes, batch processing, concurrency, and idempotency.
- Readability: names, explicit flow, and the size and responsibilities of functions and modules.
- Maintainability: actual reuse, coupling, tests, compatibility, operating costs, and evolution.

Recommend an alternative and explain its concrete benefit, cost, and conditions for reconsidering it. Avoid abstractions, dependencies, distributed services, or queues without a demonstrated need.

Ask specific questions about decisions that change behavior, data, or architecture. Include options and a reasoned recommendation; avoid vague questions such as "How do you want to implement it?" For example: "Should we retain change history, or is the current state sufficient? I recommend history if we need to reconstruct the balance at a particular date; this requires storing additional events."

Group a few priority questions and continue independent investigation. If questions remain unanswered, deliver a useful draft identifying which parts depend on each answer. Do not interpret silence as a user decision. For minor details, record a reasonable assumption without blocking the plan. If no material decisions remain open, say so without forcing questions.

## 3. Detail the impact on code and data

Prepare a concrete matrix:

| File or proposed path | Action | Class, function, or block | Planned change and rationale | Affected consumers or contracts |
| --- | --- | --- | --- | --- |

Use actions such as add, modify, or remove. Describe responsibilities, inputs, outputs, and relevant errors for new services; for existing symbols, explain which behavior changes and which contract is preserved. Listing applications or saying "modify the view" is insufficient. Include affected tests, configuration, and documentation. Do not propose files without a defined purpose or line numbers for code that does not yet exist.

For each new or modified model, document its responsibility and every affected attribute:

| Model and file | Attribute | Action and current vs. proposed definition | Type and parameters | Nullability, defaults, and validation | Relationship, index, or constraint | Existing data and rationale |
| --- | --- | --- | --- | --- | --- | --- |

Specify length, precision, choices, uniqueness, `null`, `blank`, application defaults versus database defaults, relationship targets, `on_delete`, and `related_name` when applicable. Explain what each value represents and how it is written and queried. For type changes or removals, detail compatibility and data conversion.

Inspect inherited fields, `save()`, validations, signals, and existing constraints before proposing duplicate attributes or bulk writes. Justify indexes using actual queries. If the schema is unchanged, state "No changes to models or attributes."

For schema changes, include the migration strategy, treatment of existing records, compatibility during deployment, locking risks, and recovery. Use the project's migration skill if available and applicable; verify its path before reading it. Adapt proposals to the actual framework and database versions. Describe migrations at this stage without generating or applying them.

## 4. Order implementation and verification

- Divide the work into steps with explicit dependencies. Each step connects requirements, files, expected results, and verification.
- Include relevant happy paths, boundaries, and errors; add permission, concurrency, performance, or compatibility checks when the change requires them.
- Propose commands and scenarios appropriate to the repository's environment. Distinguish checks performed during investigation from tests pending implementation. Do not claim results that were not obtained.
- Include concrete risks and mitigations, with deployment and rollback plans proportional to the change; acknowledge irreversible operations and data recovery needs.
- Do not give precise time estimates without evidence. Identify uncertainties that require a brief investigation.

## 5. Save and deliver the plan

For a new plan without an established project template, use [assets/plan-template.md](assets/plan-template.md). Adapt its length and language to the project, replace every `{{placeholder}}`, and remove authoring comments and inapplicable optional sections. Keep explicit no-change statements where required, including when models do not change. Resolve links from the final document's location. For an existing plan, preserve its useful structure and decisions instead of replacing it with the template.

Respect the location specified by the user or repository. In the absence of another convention, use `docs/features/<feature>/plan.md`, with a stable kebab-case feature id. Read that folder's `spec.md` when present and link its acceptance criteria without duplicating the specification. Update an existing plan for the same scope instead of creating duplicates, preserving prior decisions that remain valid.

If the scope includes task breakdown, save tasks in `docs/features/<feature>/tasks.md`, including acceptance criteria, affected files, dependencies, and verification for each task. Keep technical sequencing and decisions in `plan.md`; execution status belongs in `tasks.md`. Link created documents from `docs/README.md`. Create only necessary files. Do not move existing documentation unless adopting or migrating paths is part of the request.

Organize the document using these sections, adjusting its length to the change:

1. Requirement, objective, and an example of expected behavior.
2. Included scope, exclusions, and identified acceptance criteria.
3. Current state and evidence from inspected code.
4. Alternatives, recommendation, and pending or agreed decisions.
5. Affected project areas and the file/symbol matrix.
6. Models and attributes, including migrations and existing data when applicable.
7. Implementation steps, dependencies, and traceability to criteria.
8. Planned verification, risks, deployment, and recovery where applicable.
9. Assumptions and open questions, with their impact.

Record the date and status: draft if material decisions remain, or ready for implementation if sufficiently defined. Do not mark it approved without actual approval. Avoid empty tables; explicitly state when a section does not apply.

Before delivery, check that every criterion has a step and a verification, that referenced existing paths were inspected, and that model changes explain what happens to existing data. Summarize the recommendation, link the plan, and present only questions that still require an answer.
