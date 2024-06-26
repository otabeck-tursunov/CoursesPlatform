from django.db import models


class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    profession = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return self.full_name


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=255)

    subCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    duration = models.DurationField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image_path = models.ImageField(upload_to='images/', blank=True, null=True)
    students_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(default=5)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title


class Section(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    videos_count = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_path = models.URLField(blank=True, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    duration = models.DurationField(blank=True, null=True)

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return self.title
