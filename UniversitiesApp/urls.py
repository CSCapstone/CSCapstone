"""
UniversitiesApp URL Configuration

Created by Jacob Dunbar on 11/5/2016.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^universities$', views.getUniversities, name='Universities'),
    url(r'^university$', views.getUniversity, name='University'),
    url(r'^universityform$', views.getUniversityForm, name='UniversityForm'),
    url(r'^universityformsuccess$', views.getUniversityFormSuccess, name='UniversityFormSuccess'),
    url(r'^joinuniversity$', views.joinUniversity, name='JoinUniversity'),
    url(r'^unjoinuniversity$', views.unjoinUniversity, name='UnjoinUniversity'),
]