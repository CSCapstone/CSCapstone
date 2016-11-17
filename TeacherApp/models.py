from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(
        max_length = 120,
        null = True,
        blank = True,
    )
    last_name = models.CharField(
        max_length = 120,
        null = True,
        blank = True,
    )
    university = models.CharField(
        max_length = 120,
        null = True,
        blank = True,
    )
    phone = models.CharField(
        max_length = 10,

    )
    def __str__(self):
        return self.first_name + self.last_name
