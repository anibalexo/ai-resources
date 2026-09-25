---
name: django-styleguide
description: Architecture guidance based on HackSoftware's Django Styleguide, structuring business logic into Services (writes) and Selectors (reads), thin DRF APIViews with inline serializers, BaseModel constraints, and layered testing.
---

# Django Styleguide Skill

This skill implements the architectural guidelines from [HackSoftware's Django Styleguide](https://github.com/HackSoftware/Django-Styleguide), promoting maintainable, scalable, and testable Django applications by cleanly separating domain logic from external interfaces.

## Core Philosophy

In this architecture, software is divided into two distinct layers:
1. **Core Domain**: Contains business logic, database transactions, domain rules, and queries.
2. **Interface**: Adapts external protocols (HTTP requests, CLI commands, background task brokers) to invoke core services and selectors.

```
       HTTP (DRF APIView)     Celery Tasks     Management Commands
               \                   |                  /
                \                  |                 /
                 v                 v                v
            +--------------------------------------------+
            |               INTERFACE LAYER              |
            +--------------------------------------------+
                                  |
                                  v
            +--------------------------------------------+
            |                 CORE DOMAIN                |
            |                                            |
            |   [Services]            [Selectors]        |
            |   - Writes/Mutations    - Reads/Queries    |
            |   - atomic transactions - filter/prefetch  |
            |   - full_clean()        - no mutations     |
            |                                            |
            |   [Models]                                 |
            |   - BaseModel (timestamps)                 |
            |   - DB constraints & simple clean()        |
            +--------------------------------------------+
                                  |
                                  v
                              DATABASE
```

### Where Logic Belongs

| Responsibilities | Where it belongs | What it does |
| --- | --- | --- |
| Database writes, state transitions, transactions, side effects | **Services** (`services.py`) | Function-based business operations with keyword-only arguments |
| Database reads, filters, joins, prefetching, aggregations | **Selectors** (`selectors.py`) | Pure query functions returning QuerySets or model instances |
| Data modeling, timestamps, database-level constraints | **Models** (`models.py`) | Abstract `BaseModel`, `CheckConstraint`, and simple `clean()` |
| Request parsing, permissions, formatting, status codes | **APIs** (`apis.py`) | `APIView` with nested `InputSerializer` and `OutputSerializer` |
| Asynchronous execution wrappers | **Tasks** (`tasks.py`) | Thin Celery tasks delegating work to services |

### Where Logic Must NOT Live

- **APIs & Views**: Views must not perform ORM writes or complex queries; they only validate input and call services/selectors.
- **Serializers & Forms**: Avoid overriding `ModelSerializer.create()`, `update()`, or embedding business workflows in serializer validation.
- **Model `save()` methods**: Do not hide side effects, queries, or cascading updates inside `save()`.
- **Signals**: Avoid using Django signals for business logic; reserve them only for decoupled side-effects like cache invalidation or audit streams.
- **Custom Managers / QuerySets**: Use managers for reusable query filtering helpers, but never as the repository for cross-model business logic.

---

## Quick Reference Rules

1. **Services for Writes**:
   - Define services as functions with keyword-only arguments: `def entity_action(*, param1: Type, ...) -> Model:`.
   - Call `instance.full_clean()` before `instance.save()`.
   - Wrap multi-operation writes in `with transaction.atomic():`.
   - Trigger side-effects (e.g., email, Celery tasks) from services, not models or views.
2. **Selectors for Reads**:
   - Define selectors as pure query functions: `def entity_list(*, filters=None) -> QuerySet[Entity]:`.
   - Use `select_related` and `prefetch_related` inside selectors to prevent N+1 query problems.
   - Never mutate database records inside a selector.
3. **DRF APIViews with Inline Serializers**:
   - Use standard `APIView` rather than `ModelViewSet` when business rules diverge from basic CRUD.
   - Define input and output serializers inline within the API view class to avoid coupling and leaking schemas.
4. **Model Validation**:
   - Use database constraints (`CheckConstraint`, `UniqueConstraint`) as the primary guardrails.
   - Keep `clean()` focused on intra-model field comparisons; move relational checks to the service.
5. **Standardized Error Handling**:
   - Raise `ApplicationError(message="...", extra={...})` for domain-level rule violations.
   - Use a centralized DRF exception handler to format errors into standard JSON payloads.

---

## Modular Documentation & Resources

Explore the dedicated modules for detailed guidance, templates, and examples:

### Reference Guides (`references/`)
- [Overview & Navigation](references/README.md): Index of architectural topics.
- [Core Philosophy](references/core-philosophy.md): Separation of domain core and interface layers.
- [Services and Selectors](references/services-and-selectors.md): Writing conventions, transactions, and query design.
- [Models and Validation](references/models-and-validation.md): `BaseModel`, constraints, `clean()`, and property guidelines.
- [APIs and Serializers](references/apis-and-serializers.md): `APIView`, inline serializers, filtering, and pagination.
- [Exception Handling](references/exception-handling.md): `ApplicationError` and uniform DRF error responses.
- [Testing Strategy](references/testing-strategy.md): Layered tests (`tests/services/`, `tests/selectors/`, `tests/apis/`) and factories.
- [Celery Integration](references/celery-integration.md): Background workers as interface adapters.

### Templates & Boilerplates (`assets/`)
- [Application Structure Templates](assets/app-structure/README.md): Starter code for `models.py`, `services.py`, `selectors.py`, `apis.py`, and `urls.py`.
- [Exception Handler Template](assets/errors/README.md): Centralized exception handler and `ApplicationError` definition.

### Working Examples (`examples/`)
- [Examples Overview](examples/README.md): Index of sample implementations.
- [Course Management Flow](examples/course-management/README.md): End-to-end implementation including models, services, selectors, APIs, and tests.
