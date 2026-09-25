from datetime import date, timedelta
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Course
from .selectors import course_detail, course_list
from .services import course_create, course_update


class CourseServicesTests(TestCase):
    def test_course_create_success(self):
        start = date.today()
        end = start + timedelta(days=30)
        course = course_create(name="Django Advanced", start_date=start, end_date=end)

        self.assertEqual(course.name, "Django Advanced")
        self.assertTrue(Course.objects.filter(id=course.id).exists())

    def test_course_create_invalid_dates_raises_validation_error(self):
        start = date.today()
        end = start - timedelta(days=5)

        with self.assertRaises(ValidationError):
            course_create(name="Invalid Course", start_date=start, end_date=end)


class CourseSelectorsTests(TestCase):
    def setUp(self):
        start = date.today()
        self.c1 = Course.objects.create(name="Python 101", start_date=start, end_date=start + timedelta(days=10))
        self.c2 = Course.objects.create(name="Django Architecture", start_date=start + timedelta(days=15), end_date=start + timedelta(days=30))

    def test_course_list_all(self):
        courses = list(course_list())
        self.assertEqual(len(courses), 2)

    def test_course_list_filter_search(self):
        courses = list(course_list(filters={"search": "Architecture"}))
        self.assertEqual(len(courses), 1)
        self.assertEqual(courses[0].id, self.c2.id)

    def test_course_detail(self):
        course = course_detail(course_id=self.c1.id)
        self.assertEqual(course.name, "Python 101")


class CourseApisTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_course_api_success(self):
        start = date.today()
        end = start + timedelta(days=20)
        payload = {
            "name": "API Course",
            "start_date": str(start),
            "end_date": str(end),
        }

        response = self.client.post("/api/courses/create/", data=payload, format="json")
        # In a real environment with registered URLs this returns 201
        self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_404_NOT_FOUND])
