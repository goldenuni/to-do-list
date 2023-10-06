from django.urls import path, include

from app.views import TaskListView, TaskCreateView, TaskUpdateView, TaskDoneUpdateView, TaskDeleteView

app_name = "app"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/update-done/", TaskDoneUpdateView.as_view(), name="task-confirm-done"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),

]
