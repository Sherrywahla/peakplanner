from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at")
    search_fields = ("title", "user__username")
    ordering = ("-created_at",)

admin.site.register(Note, NoteAdmin)
