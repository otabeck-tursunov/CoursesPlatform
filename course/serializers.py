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


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        category = super(CategorySerializer, self).to_representation(instance)
        subCategories = SubCategory.objects.filter(category=instance)
        serializer = CategorySubCategorySerializer(subCategories, many=True)
        category.update(
            {
                'subCategories': serializer.data
            }
        )
        return category


class CategorySubCategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

    def to_representation(self, instance):
        subCategory = super(SubCategorySerializer, self).to_representation(instance)
        courses = Course.objects.filter(subCategory=instance)
        serializer = SubCategoryCourseSerializer(courses, many=True)
        subCategory.update(
            {
                'courses': serializer.data
            }
        )
        return subCategory


class SubCategoryCourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'teacher', 'rating', 'students_count')


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def to_representation(self, instance):
        course = super(CourseSerializer, self).to_representation(instance)
        sections = Section.objects.filter(course=instance)
        serializer = CourseSectionSerializer(sections, many=True)
        course.update(
            {
                'sections': serializer.data
            }
        )
        return course


class CourseSectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = ('title', 'description', 'duration', 'videos_count')


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class SectionLessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('title', 'description', 'video_path', 'duration')
