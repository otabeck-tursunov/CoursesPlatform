import django_filters
from django_filters import FilterSet
from .models import Teacher, Course, Section


class TeacherFilter(FilterSet):
    full_name = django_filters.CharFilter(field_name="full_name", lookup_expr='icontains')
    profession = django_filters.CharFilter(field_name="profession", lookup_expr='icontains')

    class Meta:
        model = Teacher
        fields = ['full_name', 'profession']


class CourseFilter(FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr='icontains')
    description = django_filters.CharFilter(field_name="description", lookup_expr='icontains')

    class Meta:
        model = Course
        fields = ['title', 'description']


class SectionFilter(FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr='icontains')

    class Meta:
        model = Section
        fields = ['title']
