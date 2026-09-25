# Course Management Example

A complete end-to-end example demonstrating HackSoftware's Django Styleguide architecture for an educational course management domain.

## Components

- `models.py`:
  - `BaseModel`: Abstract model with timestamp audit fields.
  - `Course`: Model with a `CheckConstraint` guaranteeing that `start_date < end_date` and an intra-model `clean()` method.
- `services.py`:
  - `course_create(*, name, start_date, end_date)`: Instantiates `Course`, triggers `.full_clean()`, and saves.
  - `course_update(*, course, **data)`: Selectively updates non-side-effect fields.
- `selectors.py`:
  - `course_list(*, filters=None)`: Returns an ordered QuerySet with optional search and date filtering.
  - `course_detail(*, course_id)`: Fetches a single course with `get_object_or_404`.
- `apis.py`:
  - `CourseListApi`: DRF `APIView` with nested `FilterSerializer` and `OutputSerializer`.
  - `CourseCreateApi`: DRF `APIView` with nested `InputSerializer` and `OutputSerializer`.
- `tests.py`:
  - Layered unit tests for services, selectors, and API endpoints.

[Back to examples](../README.md) | [Back to skill](../../SKILL.md)
