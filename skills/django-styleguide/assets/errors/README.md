# Exception Handler Template

Centralized exception handling for Django REST Framework according to the HackSoftware Django Styleguide.

## What it provides

- `ApplicationError`: Base domain exception with `message` and `extra` dictionary payload.
- `custom_exception_handler`: A DRF exception handler that standardizes `ApplicationError`, Django's `ValidationError`, and DRF's `ValidationError` into a uniform JSON response format:
  ```json
  {
    "message": "Human-readable description of error.",
    "extra": {}
  }
  ```

## Usage

1. Copy `exception-handler.py.template` into your shared/common utility app (e.g. `common/errors.py`).
2. Register it in `settings.py`:
   ```python
   REST_FRAMEWORK = {
       "EXCEPTION_HANDLER": "common.errors.custom_exception_handler",
   }
   ```

[Back to skill](../../SKILL.md)
