"""ProjectsApp Models

Created by Harris Christiansen on 10/02/16.
"""
from django.db import models
from AuthenticationApp.models import MyUser
import json

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')
    programmingLanguage = models.CharField(max_length=200,default=None)
    yearsOfExperience = models.IntegerField(default=0)
    speciality = models.CharField(max_length=200,default=None)
    createdBy = models.ManyToManyField(MyUser)

    def setProgrammingLanguage(self,x):
        self.programmingLanguage = x

    def getProgrammingLanguage(self):
        return self.programmingLanguage

    def setSpeciality(self,x):
        self.speciality = x

    def getSpeciality(self):
        return self.speciality

    def __str__(self):
        return self.name


class Bookmarks(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE,default=None)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,default=None)
    objects = models.Manager()
    def __str__(self):
        return self.user.get_full_name() + " bookmarked " + self.project.name
