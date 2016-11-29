"""
CompaniesApp URL Configuration

Created by Harris Christiansen on 10/02/2016.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.getIndex, name='Index'),
    url(r'^home$', views.getHome, name='Home'),
    url(r'^table$', views.getTable, name='Table'),
    url(r'^form$', views.getForm, name='Form'),
    url(r'^update_profile$', views.profile_edit, name='UpdateMyProfile'),
]