from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "status", "due_date")
    list_filter = ("status",)
    search_fields = ("title", "user__username")
    ordering = ("-due_date",)

admin.site.register(Task, TaskAdmin)
