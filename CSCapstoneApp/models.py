"""CSCapstone Project - Universal Models

File created by Harris Christiansen on April 2, 2017.
"""
from django.db import models

class SkillTag(models.Model):
	name = models.CharField(max_length=200, default='')

	def __str__(self):
		return self.name
