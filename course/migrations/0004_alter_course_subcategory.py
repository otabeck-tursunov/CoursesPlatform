# Generated by Django 5.0.6 on 2024-06-26 12:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_remove_lesson_rating_course_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='subCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.subcategory'),
        ),
    ]
