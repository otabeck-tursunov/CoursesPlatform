from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.generics import *

from .filters import TeacherFilter, CourseFilter, SectionFilter, LessonFilter
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
            openapi.Parameter('search', openapi.IN_QUERY, description="Search by full_name and profession",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('full_name', openapi.IN_QUERY, description="Filter by full_name",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('profession', openapi.IN_QUERY, description="Filter by profession",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('ordering', openapi.IN_QUERY, description="Order by fields",
                              enum=['full_name', 'profession'], type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class TeacherDetailsAPIView(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CategoriesListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title']

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('search', openapi.IN_QUERY, description="Search by title",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('ordering', openapi.IN_QUERY, description="Order by title",
                              enum=['title'], type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CategoryDetailsAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoriesListAPIView(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['title']
    ordering_fields = ['title']

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('search', openapi.IN_QUERY, description="Search by title",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('ordering', openapi.IN_QUERY, description="Order by title",
                              type=openapi.TYPE_STRING, enum=['title'], ),
            openapi.Parameter('category_id', openapi.IN_QUERY, description="Filter by Category's ID",
                              type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id', None)
        if category_id is not None:
            get_object_or_404(Category, pk=category_id)
            return SubCategory.objects.filter(category_id=category_id)
        return SubCategory.objects.all()


class SubCategoryDetailsAPIView(RetrieveAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class CoursesListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_class = CourseFilter
    search_fields = ['title', 'description', 'subCategory']
    ordering_fields = ['title', 'duration', 'students_count', 'rating']

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('search', openapi.IN_QUERY, type=openapi.TYPE_STRING,
                              description="Search by title, description, teacher and subcategory."),
            openapi.Parameter('title', openapi.IN_QUERY, type=openapi.TYPE_STRING,
                              description="Search by title"),
            openapi.Parameter('description', openapi.IN_QUERY, type=openapi.TYPE_STRING,
                              description="Search by description"),
            openapi.Parameter('ordering', openapi.IN_QUERY, type=openapi.TYPE_STRING,
                              description="Order by title, duration, students_count, rating",
                              enum=['title', 'duration', 'students_count', 'rating'], ),
            openapi.Parameter('subCategory_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER,
                              description="Filter by SubCategory's ID", ),
            openapi.Parameter('category_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER,
                              description="Filter by Category's ID", ),
            openapi.Parameter('teacher_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER,
                              description='Filter by Teacher\'s ID')

        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        courses = Course.objects.all()

        subCategory_id = self.request.query_params.get('subCategory_id', None)
        if subCategory_id is not None:
            get_object_or_404(SubCategory, pk=subCategory_id)
            courses = courses.filter(subCategory_id=subCategory_id)

        category_id = self.request.query_params.get('category_id', None)
        if category_id is not None:
            get_object_or_404(Category, pk=category_id)
            courses = courses.filter(subCategory__category_id=category_id)

        teacher_id = self.request.query_params.get('teacher_id', None)
        if teacher_id is not None:
            get_object_or_404(Teacher, pk=teacher_id)
            courses = courses.filter(teacher_id=teacher_id)
        return courses


class CourseDetailsAPIView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class SectionsListAPIView(ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_class = SectionFilter
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'duration', 'videos_count']

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('search', openapi.IN_QUERY, type=openapi.TYPE_STRING,
                              description='Search by title, description'),
            openapi.Parameter('title', openapi.IN_QUERY, type=openapi.TYPE_STRING, description="Search by title"),
            openapi.Parameter('course_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER,
                              description='Filter by Course\'s ID'),
            openapi.Parameter('ordering', openapi.IN_QUERY, type=openapi.TYPE_STRING,
                              description="Order by title, duration, videos_count",
                              enum=['title', 'duration', 'videos_count']),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        sections = Section.objects.all()
        course_id = self.request.query_params.get('course_id', None)
        if course_id is not None:
            get_object_or_404(Course, pk=course_id)
            sections = sections.filter(course_id=course_id)
        return sections


class SectionDetailsAPIView(RetrieveAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class LessonsListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_class = LessonFilter
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'duration']

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('search', openapi.IN_QUERY, type=openapi.TYPE_STRING,
                              description="Search by title, description"),
            openapi.Parameter('title', openapi.IN_QUERY, type=openapi.TYPE_STRING, description="Search by title"),
            openapi.Parameter('ordering', openapi.IN_QUERY, type=openapi.TYPE_STRING,
                              description="Order by title, duration", enum=['title', 'duration']),
            openapi.Parameter('course_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER,
                              description="Filter by Course\'s ID"),
            openapi.Parameter('section_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER,
                              description="Filter by Section's ID"),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        lessons = Lesson.objects.all()

        course_id = self.request.query_params.get('course_id', None)
        if course_id is not None:
            get_object_or_404(Course, pk=course_id)
            lessons = lessons.filter(section__course_id=course_id)

        section_id = self.request.query_params.get('section_id', None)
        if section_id is not None:
            get_object_or_404(Section, pk=section_id)
            lessons = lessons.filter(section_id=section_id)
        return lessons


class LessonDetailsAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
