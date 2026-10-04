from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'priority', 'due_date', 'completed', 'created_at')
    list_filter = ('completed', 'priority', 'category', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('completed', 'priority')
