"""GroupsApp Models

Created by Naman Patwari on 10/10/2016.
"""
from django.db import models
from AuthenticationApp.models import MyUser
from ProjectsApp.models import Project
from uuid import uuid4

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    members = models.ManyToManyField(MyUser, related_name="members")
    requests = models.ManyToManyField(MyUser, related_name="requests")
    project = models.OneToOneField(Project, on_delete=models.CASCADE, default="", primary_key=False, null=True)

    def __str__(self):
    	return self.name
    
    def aggregate_skills(self):
        list = [];
        for member in self.members.all():
            if (member.is_student):
                for lang in member.student.languages.all():
                    if not lang.name in list:
                        list.append(lang.name)
        phrase = "";
        val = 0;
        for item in list:
            val += 1
            phrase += item
            if (val < len(list)):
                phrase += ", " 
        return phrase
	
class Comment(models.Model):
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	poster = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	text = models.CharField(max_length=500)
	stamp = models.DateTimeField(auto_now_add=True)
	cid = models.CharField(max_length=100, blank=True, unique=True, default=uuid4)