from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm

# Create your views here.


# Project model list view
def list_projects(request):
    projects = Project.objects.all()
    context = {
        "list_projects": projects,
    }
    return render(request, "projects/list.html", context)


# task list view
@login_required
def show_project(request, id):
    tasks = get_object_or_404(Project, id=id)
    # def show_project(request, id):
    #     tasks = Task.objects.filter(assignee=request.user, id=id)
    context = {
        "task_list": tasks,
    }
    return render(request, "projects/details.html", context)


# Protect View
@login_required
def owner_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "list_projects": projects,
    }
    return render(request, "projects/list.html", context)


# Create Project
@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            form.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
    context = {
        "form": form,
    }
    return render(request, "projects/create.html", context)
