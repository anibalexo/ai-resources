# Implementation tasks: {{feature_title}}

<!-- Authoring notes: replace every {{placeholder}} and remove these notes.
Organize tasks logically by layer or dependency. Check off tasks as they are
completed: [ ] -> [x]. Track verification commands and acceptance criteria. -->

Feature id: {{stable_kebab_case_id}}
Plan: {{link_to_plan_md}}
Specification: {{link_to_spec_md}}
Status: In Progress
Updated: {{date_of_this_revision}}

---

## Task Overview & Progress

- [ ] **Phase 1: Models & Data Migrations**
- [ ] **Phase 2: Domain Services & Business Logic**
- [ ] **Phase 3: Selectors & Query Layer**
- [ ] **Phase 4: Interface & Entry Points (APIs / Tasks / Commands)**
- [ ] **Phase 5: Verification, Tests & Documentation**

---

## Phase 1: Models & Migrations

> Focus on zero-downtime schema changes, constraint definitions, and database migrations.

- [ ] **Task 1.1: {{model_task_title}}**
  - **Description**: {{description_of_model_or_field_change}}
  - **Files**: `{{app}}/models.py`
  - **Criteria**: {{acceptance_id}}
  - **Safe migration note**: {{backward_compatibility_or_safe_migration_plan}}
  - **Verification**: `python manage.py makemigrations --dry-run && python manage.py test {{app}}.tests.test_models`

---

## Phase 2: Domain Services (Writes & Business Logic)

> Focus on pure functions with keyword-only arguments handling transactions, validation, and side effects.

- [ ] **Task 2.1: {{service_task_title}}**
  - **Description**: {{description_of_service_function_and_business_rules}}
  - **Signature**: `def {{service_name}}(*, {{args}}) -> {{return_type}}:`
  - **Files**: `{{app}}/services/{{service_file}}.py`
  - **Validation & Errors**: Raise `ApplicationError` for business rule violations.
  - **Criteria**: {{acceptance_id}}
  - **Verification**: `pytest {{app}}/tests/services/test_{{service_file}}.py`

---

## Phase 3: Selectors (Reads & Query Optimization)

> Focus on pure query functions returning QuerySets or model instances with proper prefetching.

- [ ] **Task 3.1: {{selector_task_title}}**
  - **Description**: {{description_of_selector_function_and_filters}}
  - **Signature**: `def {{selector_name}}(*, {{args}}) -> QuerySet[{{Model}}]`
  - **Files**: `{{app}}/selectors/{{selector_file}}.py`
  - **Optimization**: Use `select_related` / `prefetch_related` to prevent N+1 queries.
  - **Criteria**: {{acceptance_id}}
  - **Verification**: `pytest {{app}}/tests/selectors/test_{{selector_file}}.py`

---

## Phase 4: Interface & Entry Points

> Focus on thin APIViews with inline serializers, Celery tasks, forms, or management commands.

- [ ] **Task 4.1: {{api_or_interface_task_title}}**
  - **Description**: {{description_of_endpoint_or_task}}
  - **Files**: `{{app}}/apis/{{api_file}}.py`, `{{app}}/urls.py`
  - **Input / Output Serializers**: Inline serializer definitions; delegate mutation to service or read to selector.
  - **Criteria**: {{acceptance_id}}
  - **Verification**: `pytest {{app}}/tests/apis/test_{{api_file}}.py`

---

## Phase 5: Verification, Tests & Documentation

> Focus on full test suite execution, security checks, and user/API documentation.

- [ ] **Task 5.1: End-to-end and regression tests**
  - **Description**: Verify end-to-end integration and ensure existing test suite passes without regressions.
  - **Command**: `pytest`
  - **Criteria**: All acceptance criteria
- [ ] **Task 5.2: Documentation and usage guides**
  - **Description**: Update API documentation, feature guides, or project README where applicable.
  - **Files**: `docs/features/{{stable_kebab_case_id}}/README.md` or relevant guides.
