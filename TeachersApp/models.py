from django.db import models
from UniversitiesApp.models import University

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=30)
    university = models.ManyToManyField(University)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name
