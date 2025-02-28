from django.urls import path
from .views import note_list, note_create, note_update, note_delete

urlpatterns = [
    path("", note_list, name="notes"),
    path("create/", note_create, name="note_create"),
    path("<int:note_id>/edit/", note_update, name="note_update"),
    path("<int:note_id>/delete/", note_delete, name="note_delete"),
]
