from django.urls import path
from .views import reminder_list, reminder_create, reminder_update, reminder_delete

urlpatterns = [
    path("", reminder_list, name="reminders"),
    path("create/", reminder_create, name="reminder_create"),
    path("<int:reminder_id>/edit/", reminder_update, name="reminder_update"),
    path("<int:reminder_id>/delete/", reminder_delete, name="reminder_delete"),
]
