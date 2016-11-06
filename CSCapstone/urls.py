"""CSCapstone Master URL Configuration

Created by Harris Christiansen on 9/18/16.

For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^', include('AuthenticationApp.urls')),
	url(r'^', include('CSCapstoneApp.urls')),
	url(r'^', include('ProjectsApp.urls')),
    url(r'^', include('CompaniesApp.urls')),
    url(r'^', include('GroupsApp.urls')),
	url(r'^', include('UniversitiesApp.urls')),
]
