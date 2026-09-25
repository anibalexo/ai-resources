from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .selectors import course_detail, course_list
from .services import course_create, course_update


class CourseListApi(APIView):
    """
    Endpoint for listing and searching courses.
    """
    class FilterSerializer(serializers.Serializer):
        search = serializers.CharField(required=False, allow_null=True)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        description = serializers.CharField()
        start_date = serializers.DateField()
        end_date = serializers.DateField()
        has_started = serializers.BooleanField()
        has_finished = serializers.BooleanField()

    def get(self, request):
        filter_serializer = self.FilterSerializer(data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)

        courses = course_list(filters=filter_serializer.validated_data)
        data = self.OutputSerializer(courses, many=True).data

        return Response(data, status=status.HTTP_200_OK)


class CourseCreateApi(APIView):
    """
    Endpoint for creating a new course.
    """
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255)
        description = serializers.CharField(required=False, default="")
        start_date = serializers.DateField()
        end_date = serializers.DateField()

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        start_date = serializers.DateField()
        end_date = serializers.DateField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        course = course_create(**serializer.validated_data)
        data = self.OutputSerializer(course).data

        return Response(data, status=status.HTTP_201_CREATED)
