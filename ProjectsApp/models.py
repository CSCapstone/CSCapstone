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
    	self.programmingLanguage = json.dumps(x)

    def getProgrammingLanguage(self):
    	return json.loads(self.programmingLanguage)

    def setSpeciality(self,x):
    	self.speciality = json.dumps(x)

    def getSpeciality(self):
    	return json.loads(self.speciality)

    def __str__(self):
        return self.name

class Bookmarks(models.Model):
    user = models.OneToOneField(MyUser)
    project = models.OneToOneField(Project)
    def __str__(self):
        return self.user.get_full_name() + " : " + project.name
        