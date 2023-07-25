from django.shortcuts import render, get_object_or_404

# from .models import Task
from .models import Project
from django.contrib.auth.decorators import login_required


# Create your views here.
# task list view
@login_required
def show_project(request, id):
    tasks = get_object_or_404(Project, id=id)
    # def show_project(request, id):
    #     tasks = Task.objects.filter(assignee=request.user, id=id)
    context = {
        "task_list": tasks,
    }
    return render(request, "tasks/details.html", context)
