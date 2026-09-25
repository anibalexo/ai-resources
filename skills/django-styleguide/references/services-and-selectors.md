# Services and Selectors

The cornerstone of the HackSoftware architecture is dividing business logic into **Services** (mutations/writes) and **Selectors** (queries/reads).

## Services (Writing & Mutating)

A service is a function responsible for creating, updating, or deleting data, orchestrating business logic, and executing side effects.

### Rules for Services

1. **Function-based**: Prefer plain Python functions over classes. Use class-based services only when a stateful workflow, strategy pattern, or complex multi-step pipeline justifies it.
2. **Keyword-only Arguments**: Enforce keyword arguments by placing `*` as the first parameter. This ensures calls are explicit and safe against argument order refactorings:
   ```python
   def course_create(*, name: str, start_date: date, end_date: date) -> Course:
       ...
   ```
3. **Explicit Validation**: Instantiate the model, call `.full_clean()`, and then call `.save()`:
   ```python
   def course_create(*, name: str, start_date: date, end_date: date) -> Course:
       course = Course(name=name, start_date=start_date, end_date=end_date)
       course.full_clean()
       course.save()
       return course
   ```
4. **Transaction Boundaries**: When a service modifies multiple tables or triggers side effects, wrap operations in `transaction.atomic()`:
   ```python
   from django.db import transaction

   def student_enroll(*, student: Student, course: Course) -> Enrollment:
       with transaction.atomic():
           enrollment = Enrollment(student=student, course=course)
           enrollment.full_clean()
           enrollment.save()
           
           course.enrolled_count += 1
           course.full_clean()
           course.save()
           
           transaction.on_commit(lambda: send_welcome_email(student=student, course=course))
           
       return enrollment
   ```
5. **Handling Updates with Services**:
   When updating records, accept optional keyword arguments and selectively update fields:
   ```python
   def course_update(*, course: Course, **data) -> Course:
       non_side_effect_fields = ["name", "description", "start_date", "end_date"]
       has_updated = False

       for field in non_side_effect_fields:
           if field in data and getattr(course, field) != data[field]:
               setattr(course, field, data[field])
               has_updated = True

       if has_updated:
           course.full_clean()
           course.save()

       return course
   ```

## Selectors (Reading & Querying)

A selector is a function responsible for querying the database and returning QuerySets or model instances.

### Rules for Selectors

1. **No Mutations**: Selectors must never modify the database state.
2. **Prevent N+1 Queries**: Encapsulate required `select_related` and `prefetch_related` calls inside the selector:
   ```python
   def course_list(*, user: User | None = None) -> QuerySet[Course]:
       qs = Course.objects.select_related("instructor").prefetch_related("tags")
       if user and not user.is_staff:
           qs = qs.filter(is_published=True)

       return qs
   ```
3. **Single Object Selectors**: Use `get_object_or_404` or return `None` explicitly:
   ```python
   from django.shortcuts import get_object_or_404

   def course_detail(*, course_id: int) -> Course:
       return get_object_or_404(
           Course.objects.select_related("instructor"),
           id=course_id
       )
   ```
4. **Filtering with `django-filter`**:
   Complex filtering should be encapsulated within selector functions, either using `django-filter` FilterSets or custom query parameters.

## Directory Structure Options

For small apps:
```text
my_app/
  services.py
  selectors.py
```

For large apps:
```text
my_app/
  services/
    __init__.py
    courses.py
    enrollments.py
  selectors/
    __init__.py
    courses.py
    enrollments.py
```

[Back to references](README.md) | [Back to skill](../SKILL.md)
