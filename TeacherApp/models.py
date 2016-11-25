from __future__ import unicode_literals

from django.db import models
from AuthenticationApp.models import MyUser
from UniversityApp.models import University
from UniversityApp.models import Course
# Create your models here.

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="static/teacherimages", default=0)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course) 
    contact_info=models.CharField(max_length=300)
    students = models.ManyToManyField(MyUser)

    def __str__(self):
        return self.name

