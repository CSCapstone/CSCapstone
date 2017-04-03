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
	url(r"^search/", include("watson.urls", namespace="watson"), {'template_name': 'search_results.html'}),	
	url(r'^university/', include('UniversitiesApp.urls_uni')),
	url(r'^course/', include('UniversitiesApp.urls_course')),
	url(r'^', include('CSCapstoneApp.urls')),
	url(r'^projects/', include('ProjectsApp.urls')),
    url(r'^', include('CompaniesApp.urls')),
    url(r'^', include('GroupsApp.urls')),
]
