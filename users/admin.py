from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import Student


class CustomUserAdmin(UserAdmin):
    model = Student
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            'Personal info',
            {
                'fields': (
                    'first_name', 'last_name', 'email', 'role', 'birth_date', 'point', 'date_joined', 'last_login')
            }
        ),
    )


admin.site.register(Student, CustomUserAdmin)
admin.site.unregister(Group)
