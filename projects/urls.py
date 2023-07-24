from django.urls import path
from .views import owner_projects

urlpatterns = [
    path("", owner_projects, name="list_projects"),
]
