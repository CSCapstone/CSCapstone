"""
CompaniesApp Admin

Created by Jacob Dunbar on 10/2/2016.
"""
from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Company)
