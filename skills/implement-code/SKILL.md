---
name: implement-code
description: Implement code changes and features applying clean code practices, early return (guard clauses), explicit type hints, readability, and maintainability. Use when writing, modifying, or refactoring code to satisfy tasks, specifications, or plans.
---

# Implement code

Turn tasks, specifications, or technical plans into clean, readable, and maintainable code. Ground changes in the repository's existing conventions and architecture, keeping the diff focused strictly on the requested behavior.

## Core practices

### 1. Early return and guard clauses

- Handle edge cases, invalid inputs, authorization checks, and preconditions at the beginning of the function or method.
- Return, break, continue, or raise early when preconditions fail instead of nesting logic in multiple levels of `if/else` blocks.
- Keep the primary flow ("happy path") at the shallowest indentation level.
- Avoid deep conditional nesting ("arrow anti-pattern" or "pyramid of doom"). If nested conditionals are unavoidable, extract the inner condition into a descriptive helper function.

### 2. Readability and clarity

- Choose intention-revealing, unambiguous names for functions, variables, parameters, and classes. Avoid cryptic abbreviations or single-letter names except in standard loop counters.
- Write functions and methods that do one thing well (single responsibility). Break down large procedures into cohesive, well-named units.
- Avoid "magic numbers" and "magic strings". Replace raw literal values in conditionals or logic with named constants or enumerations (`Enum`, `StrEnum`, or framework choices like Django's `TextChoices`/`IntegerChoices`).
- Prefer explicit control flow over clever, compressed one-liners that obscure intent or complicate debugging.
- Add comments only to explain non-obvious business logic, technical trade-offs, or upstream constraints. Do not write redundant comments that merely paraphrase what the code does.

### 3. Maintainability and low coupling

- Keep interfaces and function signatures minimal and cohesive. Pass only the data a function needs to perform its job.
- **Avoid argument mutation:** Treat parameters as read-only. Do not mutate input collections (lists, dicts) or objects in-place unless mutating the state is the explicit, documented contract of the method. Prefer returning new structures or copies.
- **Separation of concerns (Thin controllers/views & Service layer):** Keep transport layers (HTTP views, REST endpoints, serializers, CLI commands) thin. Encapsulate core business logic, complex queries, and third-party integrations into cohesive service functions or domain modules that can be tested and reused independently of the request/response lifecycle.
- Minimize mutable shared state, global variables, and hidden side effects.
- Avoid premature abstractions, speculative interfaces, or excessive design patterns where simple, direct code suffices (YAGNI).
- Adhere to the host project's idioms, naming patterns, file organization, and established conventions.

### 4. Explicit type hints and circular import handling

- Add explicit type annotations to function parameters, return values, and class attributes to establish clear contracts and aid static verification.
- **Do not discard type hints** when facing circular import issues. Instead, apply the standard and idiomatic pattern:
  - In Python, the industry standard (PEP 563 / PEP 484) to resolve circular dependencies caused by type annotations is using `from __future__ import annotations` and guarding type imports behind `typing.TYPE_CHECKING`:

```python
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # This import only executes during static analysis (IDE / mypy / linters).
    # At Python runtime, TYPE_CHECKING is False, so it never executes or causes circular imports.
    from users.services import UserService
    from orders.models import Order


def process_order(order: Order, service: UserService) -> bool:
    # Type hints, autocomplete, and static checks remain 100% intact
    if not order.is_valid:
        return False

    return service.execute(order)
```

- **Handling circular dependencies at runtime:**
  If a function genuinely needs to instantiate or invoke methods on that class during runtime execution (not only for static type hints):
  - **Architectural solution (Recommended):** A circular import often indicates tight coupling. The clean solution is to extract the shared interface, dataclass, model, or helper logic into a third common module (e.g., `interfaces.py`, `types.py`, or `common.py`).
  - **Pragmatic fallback (Last resort):** If refactoring the architecture is outside the authorized scope, import locally inside the function, but preserve the static type hint in the signature with `if TYPE_CHECKING:`:

```python
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from orders.models import Order  # For static type hint in the signature


def handle_order(order: Order) -> None:
    from orders.models import OrderCalculator  # Runtime only as a last resort
    ...
```

### 5. Atomic operations and idempotency

- When an operation performs multiple dependent writes or state transitions, encapsulate them in an atomic transaction (e.g., `with transaction.atomic():`) to prevent partial failure or inconsistent database states.
- Design critical workflows (state updates, third-party payment processing, webhook handling) to be idempotent or protected against duplicate executions.

### 6. Robust error handling

- Catch specific exceptions rather than catching all exceptions broadly.
- Never suppress errors silently; log or handle failures with actionable context.
- Ensure resources such as file handles, database connections, and locks are deterministically released (using language constructs like `with`, `using`, or `try/finally`).

### 7. Security boundaries and safe data handling

- **Zero hardcoded secrets:** Never embed passwords, API keys, private tokens, webhook secrets, or private environment URLs directly in code or test fixtures. Always retrieve sensitive credentials via environment variables, runtime configuration, or project-established secrets management.
- **Injection prevention:** Never concatenate or interpolate untrusted external inputs directly into dynamic execution contexts (such as database queries, system shell commands, filesystem paths, or code evaluations). Use parameterized queries, ORM query builders, or safe APIs provided by the platform.
- **Input validation at boundaries:** Validate, sanitize, and constrain external inputs (types, allowed ranges, expected formats) at entry points before passing them to internal business logic.

## Implementation procedure

1. **Review requirements and current code.** Read the relevant task from `tasks.md`, `plan.md`, or the prompt. Inspect existing related files, contracts, and tests. Preserve uncommitted changes unrelated to the task.
2. **Implement in dependency order.** Work sequentially through tasks or dependencies. Apply early returns, type annotations, and maintainable structure as code is written or modified, rather than planning to clean it up later.
3. **Keep changes scoped and preserve context.** Modify only the files and symbols necessary for the task. Do not reformat unrelated code, introduce unrequested dependencies, or alter established public APIs unless required by the plan. Strictly preserve preexisting docstrings, business logic comments, and surrounding code.
4. **Verify behavior.** Run existing test suites, execute targeted checks for the changed paths, and confirm that all acceptance criteria are met. If unexpected test failures occur, investigate and resolve them before finishing.

## Deliverable

Deliver the modified or created code alongside a concise summary explaining:
- The changes implemented and how they fulfill the acceptance criteria.
- Design decisions made, highlighting guard clauses, typing contracts, and structural simplifications.
- Verification results and test commands executed.

## Requirements and example

Designed for Codex with repository access and, when available, the project's runtime and test environment. No external packages are required by this skill.

Example: "Use $implement-code to implement the order cancellation handler in src/orders/service.py according to tasks.md. Apply guard clauses, clear naming, explicit type hints, and maintainable structure, and verify the result."
