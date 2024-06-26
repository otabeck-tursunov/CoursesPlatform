from django.urls import path
from .views import *

urlpatterns = [
    path('teachers/', TeachersListAPIView.as_view()),
    path('teachers/<int:pk>/', TeacherDetailsAPIView.as_view()),
]
