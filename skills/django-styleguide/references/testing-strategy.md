# Testing Strategy

Because business logic is split cleanly into distinct layers, tests can also be partitioned cleanly without complex mocking.

## Test Directory Organization

Mirror the code organization inside each app's `tests/` package:

```text
my_app/
  tests/
    __init__.py
    factories.py
    services/
      __init__.py
      test_course_create.py
      test_student_enroll.py
    selectors/
      __init__.py
      test_course_list.py
      test_course_detail.py
    apis/
      __init__.py
      test_course_create_api.py
      test_course_list_api.py
    models/
      __init__.py
      test_course_constraints.py
```

## What to Test in Each Layer

### 1. Services Tests
- Test domain business logic and validation.
- Assert database mutations occur correctly.
- Test that transactions roll back on error.
- Verify side-effects (e.g., mock outgoing emails or task dispatches).
- **Rule**: Hit the real test database. Do not mock the Django ORM inside service tests.

### 2. Selectors Tests
- Test filtering, ordering, and exclusions.
- Assert that relations are efficiently fetched and N+1 queries are prevented (`self.assertNumQueries(...)`).
- Verify edge cases (empty result sets, inactive/deleted records).

### 3. API Tests
- Test HTTP status codes (200, 201, 400, 403, 404).
- Test request payload validation and error responses.
- Test authentication and permission policies.
- Assert response contract matches `OutputSerializer`.

### 4. Model Tests
- Test `CheckConstraint` and `UniqueConstraint` violations.
- Test model `clean()` rules.

## Factories over Fixtures

Avoid static JSON or YAML fixtures. Use `factory_boy` or explicit factory functions:

```python
import factory
from django.utils import timezone
from courses.models import Course


class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course

    name = factory.Sequence(lambda n: f"Course {n}")
    start_date = factory.LazyFunction(lambda: timezone.now().date())
    end_date = factory.LazyAttribute(
        lambda obj: obj.start_date + timezone.timedelta(days=30)
    )
```

[Back to references](README.md) | [Back to skill](../SKILL.md)
