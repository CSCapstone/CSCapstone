"""
UniversitiesApp Apps

Created by Jacob Dunbar on 11/5/2016.
"""
from django.apps import AppConfig
from watson import search as watson

class UniversityConfig(AppConfig):
	name = 'UniversitiesApp'
	def ready(self):
		University = self.get_model("University")
		Course = self.get_model("Course")
		watson.register(University)
		watson.register(Course)
		#watson.register(University, fields=("slug","name",))
		# watson.register(University, exclude=("field1", "field2",))
