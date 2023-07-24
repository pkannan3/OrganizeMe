from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.


# Project model list view
def list_projects(request):
    projects = Project.objects.all()
    context = {
        "list_projects": projects,
    }
    return render(request, "projects/list.html", context)


# Protect View
@login_required
def owner_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "list_projects": projects,
    }
    return render(request, "projects/list.html", context)
