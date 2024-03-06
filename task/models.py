from django.db import models
from datetime import date

class Task(models.Model):
    title = models.CharField(max_length=30, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    task_date = models.DateField(default=date.today)
    due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(default=3)

    def __str__(self):
        return f'{self.title}'