from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course, Module, UserProfile, Progress


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_by', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'created_by')


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'module_type', 'course', 'order', 'created_at')
    search_fields = ('title', 'description', 'module_type')
    list_filter = ('module_type', 'course', 'created_at')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ('user__username', 'role')
    list_filter = ('role',)


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'module', 'completed', 'score')
    search_fields = ('user__username', 'module__title')
    list_filter = ('completed', 'score')
