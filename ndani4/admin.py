from django.contrib import admin
from .models import Task
# from django.contrib.auth.admin import UserAdmin


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'deadline', 'created_at')  # Fields to display in the admin
    list_filter = ('deadline',)  # Filter options in the admin
    search_fields = ('title', 'description')  # Searchable fields
    



