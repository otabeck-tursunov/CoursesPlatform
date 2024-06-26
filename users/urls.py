from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token-refresh/', TokenRefreshView.as_view()),

    path('register/', StudentCreateAPIView.as_view()),
    path('my-account/', StudentRetrieveAPIView.as_view()),
    path('update-account/', StudentUpdateAPIView.as_view()),
    path('delete-account/', StudentDeleteAPIView.as_view()),
]
