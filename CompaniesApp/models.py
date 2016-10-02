"""
CompaniesApp Models

Created by Jacob Dunbar on 10/2/2016.
"""
from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)