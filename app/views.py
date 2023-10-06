from django.shortcuts import render
from django.views import generic

from app.models import Task


# Create your views here.
class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5
    template_name = "app/task_list.html"