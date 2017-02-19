"""
UniversitiesApp URL Configuration

Created by Jacob Dunbar on 11/5/2016.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.getUniversities, name='universities'),
	url(r'^create/$', views.editUniversity, name='university-create'),
	url(r'^(?P<slug>[-\w\d]+)/$', views.getUniversity, name='university'),
	url(r'^(?P<slug>[-\w\d]+)/edit$', views.editUniversity, name='university-edit'),

    url(r'^(?P<slug>[-\w\d]+)/join$', views.joinUniversity, name='university-join'),
    url(r'^(?P<slug>[-\w\d]+)/unjoin$', views.unjoinUniversity, name='university-unjoin'),

	url(r'^course/form$', views.courseForm, name="CourseForm"),
	url(r'^course/add$', views.addCourse, name="AddCourse"),
	url(r'^course/remove$', views.removeCourse, name="RemoveCourse"),
	url(r'^course/join$', views.joinCourse, name="JoinCourse"),
	url(r'^course/unjoin$', views.unjoinCourse, name="UnjoinCourse"),
	url(r'^course$', views.getCourse, name="Course"),    
]