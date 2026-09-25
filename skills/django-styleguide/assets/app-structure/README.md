# Application Structure Templates

Starter templates for creating or refactoring a Django app according to the HackSoftware Django Styleguide.

## Included Templates

- `models.py.template`: Includes `BaseModel` abstract class, timestamp fields, and constraints.
- `services.py.template`: Function-based services with keyword-only arguments, `full_clean()`, and atomic transactions.
- `selectors.py.template`: Query functions with `select_related`, `prefetch_related`, and filtering.
- `apis.py.template`: DRF `APIView` with nested `InputSerializer` and `OutputSerializer`.
- `urls.py.template`: Clean URL routing registering APIViews with `.as_view()`.

## Usage

Copy these files into your new app folder and replace placeholders:
```bash
cp models.py.template my_app/models.py
cp services.py.template my_app/services.py
cp selectors.py.template my_app/selectors.py
cp apis.py.template my_app/apis.py
cp urls.py.template my_app/urls.py
```

[Back to skill](../../SKILL.md)
