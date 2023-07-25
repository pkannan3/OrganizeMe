from django.urls import path
from .views import show_project

urlpatterns = [
    path("<int:id>/", show_project, name="show_project"),
]
