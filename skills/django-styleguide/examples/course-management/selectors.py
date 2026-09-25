from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from .models import Course


def course_list(*, filters: dict | None = None) -> QuerySet[Course]:
    """
    Selector responsible for fetching a list of courses.
    Applies search and ordering without mutating state.
    """
    filters = filters or {}
    qs = Course.objects.all()

    if filters.get("search"):
        qs = qs.filter(name__icontains=filters["search"])

    return qs.order_by("start_date")


def course_detail(*, course_id: int) -> Course:
    """
    Selector responsible for fetching a single course by ID.
    """
    return get_object_or_404(Course, id=course_id)
