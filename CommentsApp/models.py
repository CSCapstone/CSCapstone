from django.db import models

class Comment(models.Model):
    time = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=500)

class SubComment(models.Model):
    parent_comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
