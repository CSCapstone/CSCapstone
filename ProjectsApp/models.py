"""ProjectsApp Models

Created by Harris Christiansen on 10/02/16.
"""
from django.db import models

from CompaniesApp.models import Company
from CSCapstoneApp.models import SkillTag

class Project(models.Model):
    name = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=10000, default='')
    company = models.ForeignKey(Company, null=True)
    created_at = models.DateTimeField('date created', auto_now_add=True)
    updated_at = models.DateTimeField('date updated', auto_now_add=True)

    tags = models.ManyToManyField(SkillTag, related_name="project_set")
    
    def __str__(self):
        return self.name
    
    def getSkillsList(self):
        list = ""
        index = 0
        for skill in self.tags.all():
            index += 1
            list += skill.name
            if index < self.tags.all().count():
                list += ", "
        return list