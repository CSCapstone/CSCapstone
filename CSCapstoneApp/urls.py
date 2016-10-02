"""
CompaniesApp URL Configuration

Created by Jacob Dunbar on 10/2/2016.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.getIndex, name='Index'),
    url(r'^table$', views.getTable, name='Table'),
    url(r'^form$', views.getForm, name='Form'),
]