from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(AbstractUser):
    phone_number = models.CharField(max_length=14, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    role = models.CharField(max_length=20, default='student')
    point = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return f"Student: {self.username}"
