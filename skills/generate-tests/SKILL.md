---
name: generate-tests
description: Create and run meaningful automated tests for existing functions, modules, or changed behavior using the project's testing conventions. Use when asked to add tests, cover edge cases, or protect against a known regression. Not for broad QA strategy, load testing, or implementing new product behavior.
---

# Generate tests

Turn the expected behavior of the requested code into focused, repeatable tests that can detect meaningful regressions.

## Establish the contract

Inspect the target code, relevant callers, existing tests, test configuration, and dependency versions. Follow the project's framework, file organization, fixtures, and commands. Honor an explicitly requested framework; explain any incompatibility that prevents using it rather than silently substituting another.

Derive expected outcomes from requirements, documented contracts, and relevant usage. Existing implementation and tests are evidence, not proof of intended behavior. If the code appears defective, do not encode the suspected defect as the expected result. Explain the discrepancy and ask about an ambiguous contract only when it changes the assertions; continue with independently established cases.

Keep implementation changes outside a tests-only request. If testability requires a production change, explain the necessary change and its scope instead of introducing an unrequested refactor. With pasted code or no execution environment, provide usable test code and explicit assumptions without claiming it ran.

## Select meaningful cases

Identify the observable contract and the failure each test would detect. Choose cases based on actual risks rather than applying every category mechanically:

- Expected results for representative inputs and state transitions.
- Invalid or empty inputs when the interface accepts them or defines their rejection.
- Boundary values immediately below, at, and above a meaningful limit.
- Expected errors, including relevant side effects and state after failure.
- Ordering, repeated calls, idempotency, permissions, or concurrency when part of the contract.

Prefer a small set of discriminating cases over many examples that exercise the same behavior. Extend existing tests when appropriate. Use parameterization for cases with the same contract and distinct relevant inputs. Do not pursue a coverage percentage unless requested or required by the project.

## Implement with the existing test stack

Choose the test level that can observe the risk: isolated unit tests for local logic, integration tests for behavior that depends on database semantics or component interactions. Do not mock away the mechanism being verified.

Use independent expected values or documented invariants; avoid reproducing the implementation's algorithm to calculate assertions. Assert externally meaningful results, errors, and side effects. Assert internal call counts only when they are themselves relevant to the contract, such as avoiding duplicate payments.

Reuse fixtures and factories while keeping each case understandable. Control time, randomness, and external I/O where they would cause nondeterminism. Isolate mutable state and clean up resources through the project's normal mechanisms. Avoid arbitrary sleeps, order-dependent tests, and real external mutations. Do not replace meaningful assertions with broad snapshots or assertions that only check that execution succeeded.

## Run and assess

Run the focused tests with the project's actual command and confirm that the intended cases were collected and executed. Distinguish assertion failures from setup failures, skipped tests, and missing dependencies. Do not weaken assertions merely to make a failing implementation pass.

For a known regression, demonstrate that the test exposes the faulty behavior when the relevant version is safely available. If a fix is also authorized, verify that the same test passes after the fix. Preserve unrelated work when comparing versions; do not reset the user's workspace. For ordinary new tests, assess whether each assertion would distinguish correct behavior from the plausible failure it targets.

Run related checks when the changes or failures justify them. If execution is unavailable, report the exact limitation and command to run; never present generated tests as verified tests.

## Deliverable

Summarize the behavior covered, the expected outcomes, and the files created or updated. Provide runnable test code directly when working from a snippet. Report execution commands, results, and any unresolved contract questions or gaps. Keep explanations proportional to the task; descriptive test names can carry routine case explanations.

## Requirements and example

Designed for Codex with access to the target code and test configuration. Uses the project's testing framework and runtime; no bundled scripts or additional packages are required by this skill.

Example: "Use $generate-tests to cover the discount calculation function with the project's existing test framework. Include threshold boundaries and invalid quantities according to the documented contract, then run the focused tests."
