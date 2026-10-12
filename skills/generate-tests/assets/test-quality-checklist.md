# Automated Test Quality Checklist

Universal quality rubric to evaluate and verify automated tests before delivery across any programming language, framework, or architecture.

---

## 1. Structure & Clarity (Arrange-Act-Assert)

- [ ] **Follows AAA Pattern**: Clearly separated into **Arrange** (setup), **Act** (single primary action under test), and **Assert** (verification).
- [ ] **One Logical Concept per Test**: Each test focuses on verifying a single behavior, outcome, or invariant.
- [ ] **Descriptive Naming**: Follows `<unit>_<scenario>_<expected_result>` (e.g., `calculate_discount_when_cart_is_empty_returns_zero`) or `should_<expected>_when_<scenario>`.
- [ ] **Self-Explaining Assertions**: Assertion failures provide actionable diagnostic messages indicating what value was expected versus what was received.

---

## 2. Test Case Selection & Boundary Analysis

- [ ] **Equivalence Partitioning**: Covers representative inputs for both valid and invalid equivalence classes.
- [ ] **Boundary Value Analysis (BVA)**: Explicitly tests boundary edges (minimum, maximum, off-by-one, empty collections, zero, null/None).
- [ ] **Specific Exception Verification**: Negative tests assert the exact error type and relevant error message/code, rather than catching generic root exceptions.
- [ ] **Table-Driven / Parameterized Testing**: Repetitive input/output scenarios sharing identical contracts are organized into parameterized test tables.

---

## 3. Test Doubles & Mocking Hygiene

- [ ] **Mock Only at External Boundaries**: Mocks/stubs are restricted to non-deterministic or external boundaries (third-party APIs, remote network calls, system clocks, message queues).
- [ ] **No Over-Mocking ("Don't mock what you own")**: Internal domain entities, utility functions, and local calculations run real code rather than being mocked.
- [ ] **State over Interaction**: Assertions verify return values or state changes rather than merely asserting that internal methods were called (`assert_called_with`), unless the invocation itself is the core contract.
- [ ] **Proper Teardown**: Patches, mocks, and environment overrides are scoped locally or cleaned up after test execution.

---

## 4. Determinism & Anti-Flakiness

- [ ] **Frozen Time & Clocks**: Tests dealing with dates, timestamps, or timeouts use frozen clocks (`freezegun`, `time-machine`, fake timers) or injected clock abstractions.
- [ ] **Controlled Randomness**: Generates data using deterministic seeds or static representative fixtures rather than unbounded random numbers.
- [ ] **Zero Arbitrary Sleep**: Asynchronous operations use active polling with timeouts (`eventually`, `wait_until`) instead of arbitrary delays (`sleep(2)`).
- [ ] **Order Independence**: Every test can run independently, in parallel, or in randomized order without relying on prior test state or global leaks.
- [ ] **Isolated Storage & Transactions**: Database modifications are executed within transactions that roll back, or against isolated ephemeral test databases.

---

## 5. Execution & Truthfulness

- [ ] **Collected & Executed**: Test commands are verified against the real project test runner.
- [ ] **Honest Execution Status**: Unexecuted or simulated tests are explicitly documented as such; never reported as verified passing tests without actual execution evidence.
- [ ] **No Tautological Assertions**: Assertions do not duplicate the production implementation logic to compute the expected outcome.
