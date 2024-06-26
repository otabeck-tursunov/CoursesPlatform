import django_filters
from django_filters import FilterSet
from .models import Teacher


class TeacherFilter(FilterSet):
    full_name = django_filters.CharFilter(field_name="full_name", lookup_expr='icontains')
    profession = django_filters.CharFilter(field_name="profession", lookup_expr='icontains')

    class Meta:
        model = Teacher
        fields = ['full_name', 'profession']
