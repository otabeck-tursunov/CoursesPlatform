from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.generics import *

from .filters import TeacherFilter
from .serializers import *


class TeachersListAPIView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_class = TeacherFilter
    search_fields = ['full_name', 'profession']
    ordering_fields = ['full_name', 'profession']

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('search', openapi.IN_QUERY, description="Filter by teacher's full name and profession",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('full_name', openapi.IN_QUERY, description="Filter by teacher's full name",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('profession', openapi.IN_QUERY, description="Filter by teacher's profession",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('ordering', openapi.IN_QUERY, description="Order by teacher's fields",
                              enum=['full_name', 'profession'], type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class TeacherDetailsAPIView(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
