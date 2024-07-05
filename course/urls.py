from django.urls import path
from .views import *

urlpatterns = [
    path('teachers/', TeachersListAPIView.as_view()),
    path('teachers/<int:pk>/', TeacherDetailsAPIView.as_view()),

    path('categories/', CategoriesListAPIView.as_view()),
    path('categories/<int:pk>/', CategoryDetailsAPIView.as_view()),

    path('subCategories/', SubCategoriesListAPIView.as_view()),
    path('subCategories/<int:pk>/', SubCategoryDetailsAPIView.as_view()),

    path('courses/', CoursesListAPIView.as_view()),
    path('courses/<int:pk>/', CourseDetailsAPIView.as_view()),

    path('sections/', SectionsListAPIView.as_view()),
    path('sections/<int:pk>/', SectionDetailsAPIView.as_view()),

    path('lessons/', LessonsListAPIView.as_view()),
    path('lessons/<int:pk>/', LessonDetailsAPIView.as_view()),

    path('my-courses/', StudentCoursesListAPIView.as_view()),
    path('get-course/', StudentCourseCreateAPIView.as_view()),
]
