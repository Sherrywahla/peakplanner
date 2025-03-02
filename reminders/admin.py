from django.contrib import admin
from .models import Reminder

class ReminderAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "remind_at")
    list_filter = ("remind_at",)
    search_fields = ("title", "user__username")
    ordering = ("-remind_at",)

admin.site.register(Reminder, ReminderAdmin)
