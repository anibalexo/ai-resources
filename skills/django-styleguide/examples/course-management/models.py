from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import F, Q
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Course(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, default="")
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="course_start_date_before_end_date",
                check=Q(start_date__lt=F("end_date"))
            )
        ]

    def __str__(self) -> str:
        return self.name

    def clean(self) -> None:
        super().clean()
        if self.start_date and self.end_date and self.start_date >= self.end_date:
            raise ValidationError({"end_date": "End date cannot be on or before start date."})

    @property
    def has_started(self) -> bool:
        return timezone.now().date() >= self.start_date

    @property
    def has_finished(self) -> bool:
        return timezone.now().date() > self.end_date
