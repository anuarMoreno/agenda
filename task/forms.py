from django.forms import ModelForm, DateInput
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ('task_date',)
        widgets = {
            "due_date" : DateInput(attrs={'type':'date'})
        }