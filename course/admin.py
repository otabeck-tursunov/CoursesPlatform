from django.contrib import admin
from .models import Teacher, Category, SubCategory, Course, Section, Lesson


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'profession')
    search_fields = ('full_name', 'profession')
    list_filter = ('profession',)

    ordering = ('full_name', 'profession')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

    ordering = ('title',)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title', 'category__title')
    list_filter = ('category',)

    ordering = ('title', 'category__title')


class SectionInline(admin.StackedInline):
    model = Section
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'subCategory', 'teacher', 'duration', 'students_count', 'created_at', 'rating'
    )
    search_fields = ('title', 'subCategory', 'teacher__full_name')
    list_filter = ('subCategory', 'subCategory', 'teacher', 'rating')

    ordering = ('title', 'rating', 'created_at')
    inlines = [SectionInline]


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1


class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'duration', 'videos_count')
    search_fields = ('title', 'course__title')

    ordering = ('title', 'duration', 'videos_count')
    inlines = [LessonInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'duration')
    search_fields = ('title', 'section__title')
    ordering = ('title', 'duration')


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Section, SectionAdmin)
