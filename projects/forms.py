from django.forms import ModelForm, TextInput
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "owner",
        ]
