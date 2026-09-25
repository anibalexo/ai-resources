# Celery Integration

In the HackSoftware styleguide, background tasks (such as Celery tasks) are treated as **interface adapters**, just like HTTP APIs or management commands.

## Core Rule: Tasks Delegate to Services

Tasks should contain minimal logic. Their primary job is:
1. Unpack task parameters (usually IDs/scalars).
2. Fetch the entity or call the service directly.
3. Handle retry policies and error reporting.

```python
from celery import shared_task
from courses.models import Course
from courses.services import course_generate_certificates


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    max_retries=3
)
def generate_course_certificates_task(self, course_id: int):
    course = Course.objects.get(id=course_id)
    return course_generate_certificates(course=course)
```

## Key Guidelines

1. **Pass Primary Keys, Not Model Instances**: Serialize only primitive types (integers, strings) to Celery task queues. Never pass active Django model instances across task boundaries.
2. **Atomic Transactions & `on_commit`**:
   When dispatching tasks from inside a service, always use `transaction.on_commit()` to ensure the database transaction has committed before the worker starts processing:
   ```python
   from django.db import transaction

   def course_complete(*, course: Course) -> Course:
       with transaction.atomic():
           course.status = Course.Status.COMPLETED
           course.full_clean()
           course.save()

           transaction.on_commit(
               lambda: generate_course_certificates_task.delay(course.id)
           )

       return course
   ```
3. **Idempotence**: Design services invoked by background tasks so they can be executed multiple times safely without producing duplicate side effects.

[Back to references](README.md) | [Back to skill](../SKILL.md)
