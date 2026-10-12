---
name: generate-tests
description: Create and run meaningful automated tests applying Arrange-Act-Assert (AAA), boundary value analysis, test double hygiene, and determinism. Universal for any language, test framework, or project architecture.
---

# Generate tests

Turn the expected behavior of the target code into focused, repeatable, and maintainable automated tests that catch real regressions. Ground every test in the project's existing testing conventions, runtime, and verifiable behavioral contracts.

## 1. Establish the contract and context

- **Inspect the environment**: Read the target code, callers, existing tests, test runner configuration, and dependencies. Follow the project's testing conventions, fixtures, factories, and commands. Honor explicitly requested frameworks; explain any incompatibility rather than silently substituting another.
- **Derive true behavior**: Derive expected outcomes from requirements, specifications, and observable contracts. Existing implementation and tests are evidence, not definitive proof of intent. If the existing code appears defective, do not encode the bug as the expected result.
- **Scope discipline**: Keep production code modifications out of a tests-only request. If testability requires refactoring production code, identify the design friction and proposed scope clearly rather than introducing unrequested edits. With pasted snippets or no execution environment, provide runnable test code with explicit assumptions without claiming it ran.

## 2. Test structure: The AAA pattern

Every test must follow the **Arrange-Act-Assert (AAA)** (or *Given-When-Then*) structure to maintain readability and diagnostic clarity:

1. **Arrange (Given)**: Set up the minimal inputs, dependencies, fixtures, or state strictly required for the scenario. Keep setup local and explicit.
2. **Act (When)**: Invoke the single action, function, or method under test. A test should typically have only one primary action.
3. **Assert (Then)**: Verify the observable result, state mutation, or expected exception.

**One logical concept per test**: Verify a single cohesive behavior or invariant per test. Avoid chaining multiple unrelated actions and assertions into long procedural test scripts; multiple checks belong in separate, focused tests to ensure failures point immediately to the root defect.

## 3. Systematic case selection

Select test cases based on actual risk and formal test design techniques rather than mechanical or arbitrary checklists:

- **Equivalence Partitioning**: Divide inputs into valid and invalid equivalence classes. Select representative values from each partition instead of repeating redundant cases.
- **Boundary Value Analysis (BVA)**: Focus heavily on boundary edges where bugs cluster: minimum values, maximum values, off-by-one transitions, empty collections, zero, null/None, and threshold crossovers.
- **Parameterized / Table-Driven Tests**: When multiple cases share the same contract and execution flow with differing inputs and expected outputs, organize them into parameterized test tables (e.g., `@pytest.mark.parametrize`, `test.each`, Go table tests, `@ParameterizedTest`).
- **Strict Negative Testing**: When verifying error handling, assert the specific exception type, error code, or domain message. Never write weak assertions that catch generic root exceptions (e.g., catching `Exception` or `Error` without type verification).

## 4. Test levels and isolation

Choose the appropriate level of the testing pyramid that observes the risk at the lowest necessary cost:

- **Unit Tests (Fast, In-Memory)**: Target pure domain logic, calculations, algorithms, state machines, and validation rules. Must run completely in-memory with zero disk, network, or external process dependencies, executing in milliseconds.
- **Integration Tests (Component & Storage)**: Target interactions with persistence layers, database queries, transaction boundaries, caching, or inter-service contracts. Run against ephemeral or isolated test storage.
- **Contract & Interface Tests (Adapters & APIs)**: Target HTTP endpoints, CLI commands, task workers, and serialization layers. Verify payload contracts, status codes, headers, and authentication/permission boundaries.

## 5. Test doubles and mocking hygiene

Mocks, stubs, and fakes should simplify tests without obscuring actual behavior:

- **Mock only at system boundaries**: Restrict test doubles to external, non-deterministic, or out-of-process boundaries: third-party APIs, remote payment gateways, email delivery, message brokers, system clocks, and hardware interfaces.
- **Don't mock what you own**: Do not mock internal helper functions, private methods, or local domain entities. Run real internal code to avoid tautological tests that pass while production code fails.
- **Assert state over interactions**: Verify return values, domain state changes, and side-effect outputs rather than checking that internal methods were invoked (`assert_called_with`). Check call counts only when invocation itself is the explicit contract (e.g., guaranteeing single charge dispatch or idempotency).
- **Strict cleanup**: Ensure all patches, mock registrations, and environment variables are cleaned up deterministically after each test run.

## 6. Determinism and anti-flakiness rules

Eliminate flakiness so tests run reliably across local environments and CI/CD pipelines:

- **Frozen clocks**: For time-dependent logic (expiration, scheduling, timestamps), use frozen clocks or time-travel utilities (`freezegun`, `time-machine`, fake timers) or inject a clock abstraction. Never rely on live system clocks (`datetime.now()`, `Date.now()`).
- **Controlled randomness**: When generating dynamic data, use deterministic seeds or static representative fixtures. Avoid unseeded random numbers or uuid-dependent assertions.
- **Order independence**: Every test must run independently. Tests must never depend on the execution order or side effects of preceding tests.
- **No arbitrary sleep**: Never use static sleep calls (`sleep(2)`) to await asynchronous operations. Use active polling with timeout limits (`eventually`, `wait_for`, `awaitility`) or event completion hooks.
- **Isolated database state**: Ensure tests that modify persistent storage run inside transactions that roll back after execution, or operate against isolated schema fixtures.

## 7. Living documentation and naming conventions

Write test names that serve as executable specifications of the system:

- **Format**: Follow `<unit_under_test>_<scenario>_<expected_outcome>` (e.g., `calculate_discount_when_cart_is_empty_returns_zero`) or BDD style (`should_throw_unauthorized_when_token_is_expired`).
- **Actionable diagnostics**: When a test fails in a CI log, the combination of test name, scenario, and assertion failure message must tell the engineer what broke and why without requiring immediate inspection of the test code.

## 8. Quality verification and deliverable

Before delivering generated tests:

1. **Verify against rubric**: Review the tests using [assets/test-quality-checklist.md](assets/test-quality-checklist.md).
2. **Execute with project runner**: Run the focused tests with the project's actual command. Confirm that tests are discovered, collected, and executed cleanly.
3. **Assess regression sensitivity**: For defect fixes, confirm the test fails against the unpatched behavior and passes after the fix.
4. **Honest reporting**: Summarize the behavior covered, test files created or updated, execution commands, and exact outputs. Explicitly state if execution was unavailable; never present unverified tests as verified.

## Requirements and example

Designed for Codex with access to the target code and test configuration. Uses the project's native testing framework and runtime; no external packages are required by this skill.

Example: "Use $generate-tests to cover the order cancellation flow. Follow the AAA pattern, test boundary states, verify specific exceptions, avoid over-mocking, and run the focused suite."
