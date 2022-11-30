# django model form (docs)

from django.forms import ModelForm
from todo_app.models import Task

class TaskForm(ModelForm):
    '''Pull the 'description' column from the Task model into a form'''
    class Meta: 
        model = Task
        fields = ['description']