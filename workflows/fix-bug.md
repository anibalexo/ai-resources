# Fix a bug

## Purpose and requirements

Reproduce a reported defect, establish its cause, apply a focused correction, and verify the result. Requires the symptom, expected behavior, relevant code, and the project's runtime or test tools when execution is possible. A review-only request stops after diagnosis and proposed corrections.

## Procedure

1. **Establish scope.** Read project instructions and pending changes. Identify expected versus actual behavior, affected versions, and a representative triggering input. Reuse the issue, specification, or relevant feature documents; do not create a full feature plan for a focused fix.
2. **Reproduce and diagnose.** Use [Debug code](../skills/debug-code/SKILL.md) to trace the reachable execution path. Distinguish a reproduced defect from a conclusion based on inspection or an unconfirmed hypothesis. Check callers and existing safeguards before declaring the cause.
3. **Protect the behavior.** Use [Generate tests](../skills/generate-tests/SKILL.md) when a regression test is feasible. Run the test against the faulty behavior and verify that it fails for the established reason, not from a broken test environment. If the behavior contract is unresolved, clarify it before encoding assumptions as assertions.
4. **Correct the cause.** Apply the smallest useful change within the requested scope. Preserve unrelated work and public behavior outside the defect. Do not hide the symptom with broad exception handling or weakened assertions.
5. **Verify.** Run the reproduction and regression test after the correction, then relevant nearby checks. For intermittent defects, repeat the scenario or create a deterministic reproduction; one passing run does not prove a race is fixed. Record commands and actual results.
6. **Update and deliver.** Update an existing issue or task record when appropriate. Use [Document features](../skills/document-features/SKILL.md) if usage, limitations, or error behavior changed. Report the cause, correction, evidence, and remaining uncertainty. Do not claim deployment or publish changes as part of this workflow.

## Completion and recovery

The fix is verified when the reported failure is resolved and relevant checks pass. If reproduction or testing is blocked, report the exact limitation and next check; identify any applied correction as unverified. Do not mark an unresolved hypothesis fixed.

When investigation reveals a broader feature or schema redesign, describe the new scope and use [Plan a feature](plan-feature.md) if planning is needed. Do not silently expand a small bug fix into a redesign. If checks regress, revise your correction while preserving unrelated changes. For a review-only request, deliver findings and stop before editing code or tests.

## Example request

> Follow this workflow to fix duplicate orders after repeated checkout submission. Reproduce locally, add a regression test, apply a focused correction, and verify it. Do not deploy.
