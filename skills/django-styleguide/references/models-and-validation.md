# Models and Validation

In the HackSoftware styleguide, models define the relational schema and integrity rules, not business workflows.

## The `BaseModel`

Every project should establish an abstract `BaseModel` that standardizes primary audit timestamps:

```python
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
```

- `created_at`: Indexed with `default=timezone.now` (facilitates chronological sorting and filtering).
- `updated_at`: Automatically updated via `auto_now=True`.

## Validation Strategy

### 1. Database Constraints (Preferred)
Enforce invariants at the database level using `CheckConstraint` and `UniqueConstraint`:
```python
from django.db import models
from django.db.models import F, Q

class Course(BaseModel):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="course_start_date_before_end_date",
                check=Q(start_date__lt=F("end_date"))
            ),
            models.UniqueConstraint(
                fields=["name"],
                name="course_unique_name"
            )
        ]
```

### 2. Model `clean()` Method
Use `clean()` for validation rules that cannot be expressed easily in SQL constraints, but follow these rules:
- **Intra-model only**: Validate combinations of fields belonging directly to the instance.
- **Do not query relations**: If validation requires fetching foreign keys, reverse relations, or third-party data, move it to the service layer.
- **Always trigger via `full_clean()` in Services**: Django does not automatically call `clean()` on `save()`. The service must invoke `instance.full_clean()` before saving.

```python
from django.core.exceptions import ValidationError

class Course(BaseModel):
    ...
    def clean(self):
        super().clean()
        if self.start_date and self.end_date and self.start_date >= self.end_date:
            raise ValidationError({"end_date": "End date must be strictly after start date."})
```

## Properties vs. Selectors

When deciding whether to expose a value as a `@property` on a model or write a selector:

- **Use `@property` when**:
  - The computation only uses fields already loaded on the local instance (e.g., `full_name = f"{first_name} {last_name}"`).
  - The computation does not execute any database queries.
- **Use a Selector function when**:
  - The calculation traverses foreign keys or ManyToMany relationships.
  - The calculation would trigger an N+1 query problem if serialized in an API response.

[Back to references](README.md) | [Back to skill](../SKILL.md)
