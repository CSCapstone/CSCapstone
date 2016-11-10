from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Comment(models.Model):
    time = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=500)
