from django.db import models

# Create your models here.

class Task(models.Model):
    '''A task object will have a description of the task to complete'''
    description = models.CharField(max_length=255)

class Comment(models.Model):
    '''A comment object will have a description of the task to comment on, and will show the date and time it is creates at'''
    # id will be set for us
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)