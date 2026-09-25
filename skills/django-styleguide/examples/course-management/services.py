from datetime import date
from django.db import transaction
from .models import Course


def course_create(
    *,
    name: str,
    start_date: date,
    end_date: date,
    description: str = "",
) -> Course:
    """
    Service responsible for creating a new Course.
    Validates rules using full_clean() before persisting.
    """
    course = Course(
        name=name,
        description=description,
        start_date=start_date,
        end_date=end_date,
    )

    course.full_clean()
    course.save()

    return course


def course_update(
    *,
    course: Course,
    **data,
) -> Course:
    """
    Service responsible for updating an existing Course.
    Only updates explicitly permitted fields.
    """
    non_side_effect_fields = ["name", "description", "start_date", "end_date"]
    has_updated = False

    with transaction.atomic():
        for field in non_side_effect_fields:
            if field in data and getattr(course, field) != data[field]:
                setattr(course, field, data[field])
                has_updated = True

        if has_updated:
            course.full_clean()
            course.save()

    return course
