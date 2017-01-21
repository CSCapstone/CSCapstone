"""GroupsApp Models

Created by Naman Patwari on 10/10/2016.
"""
from django.db import models
from AuthenticationApp.models import MyUser
from uuid import uuid4

# Create your models here.
class Group(models.Model):
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=300)
	members = models.ManyToManyField(MyUser, related_name="members")
	requests = models.ManyToManyField(MyUser, related_name="requests")
    
	def __str__(self):
		return self.name
	
class Comment(models.Model):
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	poster = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	text = models.CharField(max_length=500)
	stamp = models.DateTimeField(auto_now_add=True)
	cid = models.CharField(max_length=100, blank=True, unique=True, default=uuid4)