from __future__ import unicode_literals

from django.db import models
from AuthenticationApp.models import MyUser
from UniversitiesApp.models import University
from UniversitiesApp.models import Course
# Create your models here.

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=False)
    photo = models.ImageField(upload_to="static/teacherimages", default=0)
    email=models.CharField(max_length=300)
    user_map=models.OneToOneField(
		MyUser,
		on_delete=models.CASCADE,
		null=True,
		default=None,
		)
    
    university=models.ForeignKey(University, on_delete=models.CASCADE, null=True, default=None)
    courses = models.ManyToManyField(Course) 

    def __str__(self):
        return self.name

