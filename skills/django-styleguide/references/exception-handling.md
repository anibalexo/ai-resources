# Exception Handling

Consistent error handling ensures API consumers receive structured, predictable error responses and prevents internal domain details from leaking.

## Domain Exceptions with `ApplicationError`

Define an application-level base exception to signal expected business rule violations:

```python
class ApplicationError(Exception):
    def __init__(self, message: str, extra: dict | None = None):
        super().__init__(message)
        self.message = message
        self.extra = extra or {}
```

Services raise `ApplicationError` (or domain-specific subclasses) when business rules fail:
```python
def student_enroll(*, student: Student, course: Course) -> Enrollment:
    if course.is_full:
        raise ApplicationError(
            message="Cannot enroll student in a full course.",
            extra={"course_id": course.id, "capacity": course.capacity}
        )
    ...
```

## Standardized JSON Response Format

All API errors should conform to a standard envelope:

```json
{
  "message": "Cannot enroll student in a full course.",
  "extra": {
    "course_id": 12,
    "capacity": 30
  }
}
```

For validation errors (such as field-level errors):
```json
{
  "message": "Validation error occurred.",
  "extra": {
    "fields": {
      "start_date": ["Date has wrong format."],
      "end_date": ["End date must be strictly after start date."]
    }
  }
}
```

## Centralized DRF Exception Handler

Configure DRF's `EXCEPTION_HANDLER` in `settings.py`:

```python
REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "common.errors.custom_exception_handler",
}
```

The handler converts:
1. `ApplicationError` into HTTP 400 with `message` and `extra`.
2. Django's `ValidationError` into HTTP 400 with formatted field errors.
3. DRF's `ValidationError` into HTTP 400 with unified formatting.
4. `Http404` and `PermissionDenied` into appropriate 404 and 403 responses.

[Back to references](README.md) | [Back to skill](../SKILL.md)
