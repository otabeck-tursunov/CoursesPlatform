from rest_framework.serializers import ModelSerializer
from .models import *


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_fields = ['id']

    def to_representation(self, instance):
        teacher = super(TeacherSerializer, self).to_representation(instance)
        courses = Course.objects.filter(teacher=instance)
        serializer = TeacherCourseSerializer(courses, many=True)
        teacher.update(
            {
                'courses': serializer.data
            }
        )
        return teacher


class TeacherCourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'rating', 'students_count')
