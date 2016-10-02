"""ProjectsApp URL Configuration

Created by Harris Christiansen on 10/02/16.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^projects$', views.getProjects, name='Projects'),
    url(r'^project$', views.getProject, name='Project'),
]