"""ProjectsApp Admin

Created by Harris Christiansen on 10/02/16.
"""
from django.contrib import admin

from . import models

admin.site.register(models.Project)