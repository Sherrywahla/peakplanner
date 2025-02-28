from django.urls import path
from .views import task_list, task_create, task_update, task_delete

urlpatterns = [
    path("", task_list, name="tasks"),
    path("create/", task_create, name="task_create"),
    path("<int:task_id>/edit/", task_update, name="task_update"),
    path("<int:task_id>/delete/", task_delete, name="task_delete"),
]
