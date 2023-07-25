from django.urls import path
from .views import owner_projects, create_project

urlpatterns = [
    path("", owner_projects, name="list_projects"),
    path("create/", create_project, name="create_project"),
]
