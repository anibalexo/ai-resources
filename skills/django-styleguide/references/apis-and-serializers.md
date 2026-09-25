# APIs and Serializers

In HackSoftware's styleguide, Django REST Framework (DRF) is treated strictly as an **interface adapter**. Its sole responsibility is HTTP handling, status codes, and input/output mapping.

## Why Prefer `APIView` over `ModelViewSet`?

While `ModelViewSet` provides quick scaffolding for generic CRUD, real applications quickly outgrow standard operations:
- Permissions, query filtering, and validation diverge across actions.
- Business logic leaks into `perform_create`, `perform_update`, and serializer methods.
- Tracing data flow becomes difficult due to heavy inheritance.

Using explicit `APIView` classes makes every endpoint transparent, declarative, and easy to debug.

## Inline Serializers Pattern

Instead of creating monolithic `CourseSerializer` classes used for both reading and writing, define distinct, nested serializers inside the `APIView`:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from courses.services import course_create
from courses.selectors import course_list


class CourseListApi(APIView):
    class FilterSerializer(serializers.Serializer):
        search = serializers.CharField(required=False, allow_null=True)
        is_published = serializers.BooleanField(required=False, default=True)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        start_date = serializers.DateField()
        end_date = serializers.DateField()

    def get(self, request):
        filter_serializer = self.FilterSerializer(data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)

        courses = course_list(filters=filter_serializer.validated_data)
        data = self.OutputSerializer(courses, many=True).data

        return Response(data, status=status.HTTP_200_OK)


class CourseCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255)
        start_date = serializers.DateField()
        end_date = serializers.DateField()

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        course = course_create(**serializer.validated_data)
        data = self.OutputSerializer(course).data

        return Response(data, status=status.HTTP_201_CREATED)
```

## Key Guidelines

1. **InputSerializer**: Validates format, types, and schema. It does NOT write to the database.
2. **OutputSerializer**: Formats model instances, querysets, or dictionaries into the required client contract.
3. **No `serializers.ModelSerializer` for Writes**: Write serializers should use `serializers.Serializer` to explicitly declare accepted input fields and decouple API payload changes from model fields.
4. **Pagination**: Wrap list endpoints with reusable pagination utility functions or classes when dealing with unbounded datasets.

[Back to references](README.md) | [Back to skill](../SKILL.md)
