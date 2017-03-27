"""ProjectsApp Models

Created by Harris Christiansen on 10/02/16.
"""
from django.db import models

from CompaniesApp.models import Company

class ProgrammingLanguage(models.Model):
	name = models.CharField(max_length=200, default='')

	def __str__(self):
		return self.name

class Project(models.Model):
	name = models.CharField(max_length=200, default='')
	description = models.CharField(max_length=10000, default='')
	company = models.ForeignKey(Company, null=True)
	created_at = models.DateTimeField('date created', auto_now_add=True)
	updated_at = models.DateTimeField('date updated', auto_now_add=True)

	languages = models.ManyToManyField(ProgrammingLanguage, related_name="project_set")

	def __str__(self):
		return self.name

