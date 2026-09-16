---
name: debug-code
description: Investigate suspected code defects or review code for actionable bugs using execution paths, reproducible cases, and evidence of root causes. Use for incorrect results, exceptions, broken edge cases, or explicit bug reviews, with targeted fixes when requested. Not for general style cleanup, architecture review, or performance optimization without a correctness defect.
---

# Debug code

Identify actionable defects, explain their triggering conditions and root causes, and verify focused corrections when implementation is requested.

## Define the investigation

Establish the reported symptom, expected behavior, relevant code or diff, runtime versions, and available reproduction steps. Read nearby code, callers, configuration, and existing tests as needed to understand the execution path. For a change review, consider the surrounding behavior and distinguish newly introduced defects from pre-existing issues.

Respect the requested mode. A bug review reports findings and proposed corrections; a request to fix a bug includes targeted implementation and verification. Do not turn a review into file edits or expand a fix into general cleanup. With only a snippet, identify the missing context and keep conclusions conditional where it matters.

## Establish evidence

Reproduce the symptom with the smallest representative input or existing failing test when practical. Record expected versus actual behavior, the relevant command, and the conditions needed to trigger the issue. If the expected behavior is ambiguous, use requirements and documented contracts before inferring it from the current implementation.

Trace the failure from the entry point to the incorrect operation. Check whether validation, exception handling, transactions, permissions, or upstream constraints already prevent a suspected problem. An unusual code pattern alone is not a defect.

Inspect risks relevant to the path: incorrect conditions or boundaries, missing state handling, ordering or mutation, error propagation, resource cleanup, data consistency, and concurrency. For a suspected security defect, explain the reachable input, trust boundary, and concrete consequence; avoid declaring a vulnerability solely because a safeguard is absent from the supplied snippet. Use local, non-destructive examples rather than exploiting a live service.

Separate findings by evidence:

- **Reproduced:** a test or execution demonstrates the incorrect result.
- **Supported by code inspection:** a reachable path and violated contract establish the defect, but execution has not confirmed it.
- **Unconfirmed hypothesis:** missing context or an untested condition prevents establishing the defect; state what would confirm or reject it.

Do not report hypotheses as confirmed bugs. If the environment blocks reproduction, explain that limitation and continue with supported analysis.

## Prioritize findings

For each actionable defect, provide the relevant file and line, triggering conditions, expected and actual behavior, root cause, evidence, and smallest useful correction. Rank severity by concrete consequence and reachability, separately from confidence in the diagnosis.

Prioritize data loss, unauthorized access, crashes, and incorrect core results according to their actual scope. Avoid hypothetical chains of events that are not supported by the code or context. Keep style preferences, unused code, and optional refactoring out of the bug list unless they cause a demonstrated behavioral problem. Do not invent findings to satisfy a quota.

## Correct and verify when requested

Fix the responsible mechanism rather than suppressing the symptom. Preserve unrelated behavior, public interfaces, and existing user changes. Avoid broad rewrites, catch-all error suppression, or disabling validations to make a reproduction pass.

When feasible, add or update a regression test that fails for the established reason before the correction and passes afterward. Run relevant existing checks, including nearby edge cases that the fix could affect. For intermittent failures, repeat the triggering scenario or use a deterministic reproduction where possible; one passing run does not establish that a race is fixed.

If a correction requires changing an unresolved product contract or broadening scope, report the decision needed and continue any independent diagnosis. Stop once the requested issue is addressed and relevant checks pass; leave unrelated findings as separate observations.

## Deliverable

Lead with the actionable findings or verified fix. Include evidence status, code locations, consequences, and focused proposed or applied changes. Report reproduction and validation results and any remaining uncertainty. If no actionable defect is established, say so and state the reviewed scope; do not imply the entire project is bug-free.

## Requirements and example

Designed for Codex with access to relevant code and, for reproduction, the project's runtime and test tools. No bundled scripts or additional packages are required by this skill. Supplied snippets support a more limited static review.

Example: "Use $debug-code to investigate why submitting the checkout form twice creates two orders. Trace the cause, reproduce it locally, apply a focused fix, and verify it with a regression test."
