from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from tasks.models import Task, Worker


def index_view(request: HttpRequest) -> HttpResponse:
    num_tasks = Task.objects.count()
    num_workers = Worker.objects.count()

    context = {
        "num_tasks": num_tasks,
        "num_workers": num_workers
    }
    return render(request, "index.html", context=context)
