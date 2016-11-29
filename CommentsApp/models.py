from __future__ import unicode_literals

from django.db import models


class Comment(models.Model):
    time = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=500)

    def __str__(self):
        # toString() method
        return str(self.time) + ", " + self.comment

class Sub_Comment(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=500, null=True)

    def __str__(self):
        # toString() method
        return str(self.comment_id) + ", "+ str(self.time) + ", " + self.comment