"""
CompaniesApp Models

Created by Jacob Dunbar on 10/2/2016.
"""
from django.db import models
from AuthenticationApp.models import MyUser

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    members = models.ManyToManyField(MyUser)
    
    def __str__(self):
        return self.name