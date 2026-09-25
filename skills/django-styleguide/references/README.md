# Django Styleguide References

Comprehensive guides covering each architectural area of the HackSoftware Django Styleguide.

## Topics

- [Core Philosophy](core-philosophy.md): Explains the separation between core domain and interface layers, and why logic should be kept out of views, serializers, managers, and signals.
- [Services and Selectors](services-and-selectors.md): Implementation details for function-based services (mutations) and selectors (queries), keyword-only arguments, transactions, and composition.
- [Models and Validation](models-and-validation.md): Designing `BaseModel`, database constraints, validation with `clean()` and `full_clean()`, and properties versus selectors.
- [APIs and Serializers](apis-and-serializers.md): Building lean DRF `APIView` classes, using inline input and output serializers, query parameter filtering, and pagination.
- [Exception Handling](exception-handling.md): Raising domain-specific `ApplicationError` exceptions and standardizing API error responses through custom DRF handlers.
- [Testing Strategy](testing-strategy.md): Testing each layer in isolation (`tests/services/`, `tests/selectors/`, `tests/apis/`), and setting up factories.
- [Celery Integration](celery-integration.md): Writing robust background tasks as thin wrappers calling domain services.

[Back to skill](../SKILL.md)
