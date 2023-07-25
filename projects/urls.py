from django.urls import path
from .views import owner_projects, show_project, create_project

urlpatterns = [
    path("", owner_projects, name="list_projects"),
    path("<int:id>/", show_project, name="show_project"),
    path("create/", create_project, name="create_project"),
]
