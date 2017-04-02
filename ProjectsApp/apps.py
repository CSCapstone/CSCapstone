"""ProjectsApp Apps

Created by Harris Christiansen on 10/02/16.
"""
from django.apps import AppConfig
from watson import search as watson

class ProjectsConfig(AppConfig):
	name = 'ProjectsApp'
	def ready(self):
		Project = self.get_model("Project")		
		watson.register(Project, fields=("description","name","company","tags",))
		#watson.register(University, fields=("slug","name",))
		# watson.register(University, exclude=("field1", "field2",))
