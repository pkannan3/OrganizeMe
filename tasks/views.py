from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from django.contrib.auth.decorators import login_required


# create task
@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(False)
            # Set owner to user
            task.assignee = request.user
            form.save()
            # Redirect to 'category_list'
            return redirect("list_projects")
    else:
        form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/create_task.html", context)
