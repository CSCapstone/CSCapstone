"""ProjectsApp URL Configuration

Created by Harris Christiansen on 10/02/16.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.getProjects, name='projects'),
	url(r'^create/$', views.editProject, name='project-create'),
	url(r'^search/$', views.searchProject, name='project-search'),
	url(r'^([0-9]+)$', views.getProject, name='project'),
	url(r'^([0-9]+)/edit$', views.editProject, name='project-edit'),
    url(r'^([0-9]+)/choose$', views.chooseGroup, name='project-choosegroup'),
]