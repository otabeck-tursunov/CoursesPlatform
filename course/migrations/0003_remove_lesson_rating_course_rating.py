# Generated by Django 5.0.6 on 2024-06-25 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_rename_category_course_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='rating',
        ),
        migrations.AddField(
            model_name='course',
            name='rating',
            field=models.PositiveSmallIntegerField(default=5),
        ),
    ]
