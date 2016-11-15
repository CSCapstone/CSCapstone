"""
UniversitiesApp URL Configuration

Created by Jacob Dunbar on 11/5/2016.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^university/all$', views.getUniversities, name='Universities'),
	url(r'^university/form$', views.getUniversityForm, name='UniversityForm'),
    url(r'^university/formsuccess$', views.getUniversityFormSuccess, name='UniversityFormSuccess'),
    url(r'^university/join$', views.joinUniversity, name='JoinUniversity'),
    url(r'^university/unjoin$', views.unjoinUniversity, name='UnjoinUniversity'),
	url(r'^university/course/form$', views.courseForm, name="CourseForm"),
	url(r'^university/course/add$', views.addCourse, name="AddCourse"),
	url(r'^university/course/remove$', views.removeCourse, name="RemoveCourse"),
	url(r'^university/course/join$', views.joinCourse, name="JoinCourse"),
	url(r'^university/course/unjoin$', views.unjoinCourse, name="UnjoinCourse"),
	url(r'^university/course$', views.getCourse, name="Course"),
    url(r'^university$', views.getUniversity, name='University'),
]