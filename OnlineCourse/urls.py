from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Online Courses API",
        default_version='v1',
        description="Developed by Otabek Tursunov",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="otabecktursunov@gmail.com"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),

    path('students/', include('users.urls')),
    path('courses/', include('course.urls')),

]
