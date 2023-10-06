from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from app.forms import TaskForm
from app.models import Task


# Create your views here.
class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5
    template_name = "app/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "app/task_form.html"
    success_url = reverse_lazy("todo-list:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "app/task_form.html"
    success_url = reverse_lazy("todo-list:task-list")


class TaskDoneUpdateView(generic.UpdateView):
    model = Task
    fields = ["done"]
    success_url = reverse_lazy("todo-list:task-list")


