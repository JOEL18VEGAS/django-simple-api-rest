# Django Imports.
from django.db import models


# Project Model.
class Project(models.Model):
    
    title = models.CharField(max_length=50)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    
