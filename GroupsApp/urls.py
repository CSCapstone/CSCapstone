"""GroupsApp URL

Created by Naman Patwari on 10/10/2016.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^groups$', views.getGroups, name='Groups'),
    url(r'^group$', views.getGroup, name='Group'),
    url(r'^groupform$', views.getGroupForm, name='GroupForm'),
    url(r'^groupformsuccess$', views.getGroupFormSuccess, name='GroupFormSuccess'),
    url(r'^group/join$', views.join, name='GJoin'),
    url(r'^group/unjoin$', views.unjoin, name='GUnjoin'),
]