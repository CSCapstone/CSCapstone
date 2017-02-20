"""
CompaniesApp URL Configuration

Created by Harris Christiansen on 10/02/2016.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.getIndex, name='home'),
]