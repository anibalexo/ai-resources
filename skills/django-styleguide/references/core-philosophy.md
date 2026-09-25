# Core Philosophy

The primary objective of the HackSoftware Django Styleguide is to make applications scalable, maintainable, and predictable by enforcing a clear separation of concerns.

## Core vs. Interface

An application consists of two main conceptual areas:

1. **Core Domain (Business Logic)**:
   - Contains the essential rules, workflows, data integrity constraints, and queries of your application.
   - Independent of how users or outside systems interact with it.
   - Represented by **Services**, **Selectors**, and **Models**.
2. **Interface (Adapters)**:
   - Accepts external inputs, validates formats and authentication, translates data, and invokes the core domain.
   - Handles transport-specific details (HTTP status codes, REST headers, command-line arguments, Celery queue metadata).
   - Represented by **APIs/Views**, **Serializers/Forms**, **Management Commands**, and **Celery Tasks**.

## Why Avoid Logic in Standard Django Containers?

### 1. APIs and Views
- Placing business logic in views tightly couples domain operations to the HTTP protocol.
- Logic cannot be easily reused by background tasks, management commands, or other services without mock requests.

### 2. Serializers and ModelViewSets
- Generic `ModelViewSet` and overriding `ModelSerializer.create()` or `update()` works well for basic CRUD, but deteriorates rapidly when workflows involve multi-step transactions, third-party API calls, notifications, or cross-model interactions.
- Leads to fragmented business logic split across `.validate()`, `.create()`, `.update()`, and view hooks (`perform_create`, `perform_update`).

### 3. Model `save()` Methods
- Overriding `save()` conceals side effects during routine persistence operations.
- Bulk operations (`bulk_create`, `bulk_update`) bypass `save()`, leading to subtle inconsistencies.
- Makes testing difficult because saving a model instance unexpectedly triggers emails, external calls, or cascading mutations.

### 4. Django Signals
- Signals introduce implicit coupling: reading a function does not reveal what other components execute when a model changes.
- Obscures execution order and transaction lifecycles.
- **Rule**: Limit signals to truly decoupled, cross-cutting concerns (e.g., clearing an external cache cluster or generating audit log entries). Never orchestrate business flows through signals.

### 5. Custom Managers & QuerySets
- Managers are tied to a single model class, whereas real business operations almost always span multiple models and domain entities.
- Managers should provide query shortcuts and filters (`.active()`, `.for_tenant(tenant)`), not mutate state or invoke side effects.

[Back to references](README.md) | [Back to skill](../SKILL.md)
