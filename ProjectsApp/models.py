"""ProjectsApp Models

Created by Harris Christiansen on 10/02/16.
"""
from django.db import models
from AuthenticationApp.models import MyUser
from GroupsApp.models import Group

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    created_at = models.DateTimeField('date created', auto_now_add=True)
    updated_at = models.DateTimeField('date updated', auto_now=True)
    created_by = models.ManyToManyField(MyUser, default=None,) 
    programming_language = models.CharField(max_length=100, default=None)
    experience = models.IntegerField(default=0)
    skills = models.CharField(max_length=200, default=None)
    group = models.OneToOneField(Group, null=True, default=None)

    # TODO Task 3.5: Add field for company relationship
    # TODO Task 3.5: Add fields for project qualifications (minimum required: programming language, years of experience, speciality)

    def __str__(self):
        return self.name
