"""
UniversitiesApp Admin

Created by Jacob Dunbar on 11/5/2016.
"""
from django.contrib import admin
from watson.admin import SearchAdmin

# Register your models here.
from . import models


class UniversityAdmin(SearchAdmin):
    search_fields = ("name",)

admin.site.register(models.University, UniversityAdmin)
#watson.register(YourModel)
