from django.urls import path, include

from app.views import TaskListView

app_name = "app"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
]
