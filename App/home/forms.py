from django import forms
from .models import NewTask

class TaskForm(forms.ModelForm):
    class Meta:
        model=NewTask
        fields=['title','description','completed']