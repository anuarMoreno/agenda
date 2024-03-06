from django.db import models
from datetime import date

class Contact(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    mobile = models.CharField(max_length=12, blank=False, null=False)
    phone = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(max_length=30, blank=False, null=False)
    company = models.CharField(max_length=25, blank=True, null=True)
    date_include = models.DateField(default=date.today)
    notes = models.TextField(blank=True, null=False)

    def __str__(self):
        return f'{self.name} {self.last_name}'