"""ProjectsApp URL Configuration

Created by Harris Christiansen on 10/02/16.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^project/all$', views.getProjects, name='Projects'),
    url(r'^project/form$', views.getProjectForm, name='ProjectForm'),
    url(r'^project/formsuccess$', views.getProjectFormSuccess, name='ProjectFormSuccess'),
    url(r'^project/join$', views.joinProject, name='ProjectJoin'),
    url(r'^project/unjoin$', views.unjoinProject, name='ProjectUnjoin'),
    url(r'^project$', views.getProject, name='Project'),
]