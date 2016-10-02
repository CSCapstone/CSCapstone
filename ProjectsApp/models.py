"""ProjectsApp Models

Created by Harris Christiansen on 10/02/16.
"""
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')

    def __str__(self):
        return self.name