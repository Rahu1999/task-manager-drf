from django.db import models

# Create your models here.
class TaskList(models.Model):
    title = models.CharField(max_length=80)


class Task(models.Model):
    title = models.CharField(max_length=80)
    completed = models.BooleanField(default=False)
    task_list = models.ForeignKey(TaskList,on_delete=models.CASCADE) 