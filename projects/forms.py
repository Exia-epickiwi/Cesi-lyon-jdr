from django import forms
from projects.models import Task

class createTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ("name",)