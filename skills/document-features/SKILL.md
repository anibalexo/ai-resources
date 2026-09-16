---
name: document-features
description: Create and maintain project documentation as features are added or changed, using implemented behavior and existing documentation conventions. Use alongside feature implementation or when asked to document a completed feature, update usage guides, or explain changed APIs and configuration. Not for implementation planning, unrelated documentation rewrites, or release publishing.
---

# Document features

Keep project documentation aligned with the features actually implemented. Update the existing source of truth and make new behavior discoverable to its intended readers.

## Identify the change and evidence

Read repository instructions, documentation indexes, relevant guides, and the working tree status. Establish the feature scope from the user's request and the relevant implementation, tests, and diff. When a feature is already committed, inspect the specified change or code path rather than assuming the working tree contains it. Do not attribute unrelated pending changes to the feature.

Trace the behavior that needs explanation: entry points, inputs, outputs, permissions, validation, configuration, and important failure cases. Use requirements and plans as context, then verify claims against the code. Do not describe planned behavior as available or a local implementation as already deployed. Surface discrepancies that affect the documentation instead of inventing missing behavior.

When working alongside implementation, identify documentation impact early and finalize the text after the behavior stabilizes. If only documentation is requested, keep edits within documentation and its directly related examples or docstrings; report implementation defects separately.

## Choose the right location

Follow the project's language, terminology, audience, format, and documentation tooling. Inspect existing pages before creating a new one.

| Change | Documentation to consider |
| --- | --- |
| New user capability or changed workflow | Existing feature guide or usage section, with a realistic example |
| Public API or integration contract | Maintained API source, request and response examples, permissions, and errors |
| Configuration or installation requirement | Setup guide and configuration reference, including defaults and whether a value is required |
| Data model or architectural change relevant to maintainers | Technical reference explaining responsibilities, relationships, and the reason for the design |
| Compatibility or migration requirement | Upgrade instructions and operational effects supported by the actual change |
| Release-visible change | Existing changelog convention, using an unreleased section when appropriate |

Choose only the affected surfaces; do not produce every document type for every feature. Keep the README as an entry point when detailed guides exist. Update a relevant existing page rather than creating competing explanations. Edit the source of generated documentation and use the documented generator when available; do not hand-edit generated output as the authoritative source.

If no documentation convention exists and the feature needs a dedicated explanation, create `docs/features/<feature>/usage.md`, reusing the stable kebab-case feature id used by its `spec.md`, `plan.md`, and `tasks.md`, when present. Add a link from `docs/README.md` or the established documentation index. For a small feature, a concise section in an existing document may be enough. Avoid creating a documentation framework, changelog, or hierarchy without a concrete need.

Keep shared project context in `docs/project.md`, architecture in `docs/architecture/overview.md`, relevant decisions in `docs/architecture/decisions/`, and development setup in `docs/guides/development.md` when these documents are needed and no other convention exists. Link shared material rather than copying it into each feature. Do not rewrite specifications as usage guides or mark tasks complete merely because documentation was written. Preserve existing paths unless their migration is requested.

## Write what readers need

Start with the capability, who uses it, and how to use it. Include the following only where relevant:

- Prerequisites, permissions, and required configuration.
- A concrete usage example and its expected result.
- Inputs, defaults, validation rules, and observable errors.
- Important limitations, compatibility changes, and troubleshooting grounded in the implementation.
- Technical details needed to maintain or integrate the feature, including affected contracts and data relationships.

Use the project's actual commands, parameter names, routes, and configuration keys. Clearly mark example values and placeholders. Keep examples free of credentials and private data. Distinguish an absent value from an empty value when the implementation treats them differently.

Explain externally observable behavior in user guides; reserve internal classes and functions for developer documentation where they help the reader. Prefer stable file or symbol references over line numbers likely to drift. Reuse links to canonical explanations instead of copying configuration tables or business rules across pages.

For changed behavior, revise or remove obsolete instructions in the affected pages, including examples and defaults. Preserve unrelated content. Do not invent release versions, dates, rollout status, performance claims, or successful test results. Clearly label any unresolved assumption that prevents an accurate explanation and ask only for information that materially affects it.

## Verify and finish

Check each substantive claim against the implementation or an established contract. Verify local links, referenced paths, heading anchors, and consistency of names and examples. Run the project's existing documentation lint or build when available and relevant.

Run safe local examples when practical. Do not execute examples that mutate external systems merely to validate documentation; explain which examples remain unexecuted. If a build cannot run, state the limitation and distinguish structural checks from a successful rendered build.

Finish by reporting the pages created or updated, the behavior they cover, checks performed, and any remaining gap. If the change has no meaningful documentation impact, explain why rather than adding filler. Do not publish documentation or claim that it is deployed as part of a local documentation update.

## Requirements and examples

Designed for Codex with access to the project's code and documentation. Uses existing documentation tools when present; no bundled scripts or additional packages are required by this skill. Installing the skill makes it available for matching tasks; it does not create a file watcher, Git hook, or background process.

Examples:

- "Use $document-features to document the new CSV export feature. Update the existing usage guide from the implemented behavior and link it from the documentation index."
- "Implement order history and use $document-features to update the relevant documentation before finishing."
