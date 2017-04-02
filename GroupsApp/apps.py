"""GroupsApp Apps

Created by Naman Patwari on 10/10/2016.
"""
from django.apps import AppConfig
from watson import search as watson


class GroupsConfig(AppConfig):
	name = 'GroupsApp'
	def ready(self):
		Group = self.get_model("Group")		
		watson.register(Group, fields=("description","name","group_skills",))
		#watson.register(University, fields=("slug","name",))
		# watson.register(University, exclude=("field1", "field2",))
