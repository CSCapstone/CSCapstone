"""
UniversitiesApp URL Configuration

Created by Jacob Dunbar on 11/5/2016.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.getCourses, name='courses'),
	url(r'^create$', views.editCourses, name='course-create'),
	url(r'^id$', views.getCourse, name='course'),
	url(r'^edit$', views.editCourses, name='course-edit'),

    url(r'^join$', views.joinCourse, name='course-join'),
    url(r'^unjoin$', views.unjoinCourse, name='course-unjoin'),

	# url(r'^(?P<slug>[-\w\d]+)/course$', views.getCourses, name="courses"),
	# url(r'^(?P<slug>[-\w\d]+)/course/create$', views.createCourse, name="course-create"),

	# url(r'^course/(?P<slug>[-\w\d]+)/$', views.getCourse, name="course"),
	# url(r'^course/(?P<slug>[-\w\d]+)/edit$', views.editCourse, name="course-edit"),
	# url(r'^course/(?P<slug>[-\w\d]+)/remove$', views.removeCourse, name="course-remove"),
		
	# url(r'^course/(?P<slug>[-\w\d]+)/join$', views.joinCourse, name="course-join"),
	# url(r'^course/(?P<slug>[-\w\d]+)/unjoin$', views.unjoinCourse, name="course-unjoin"),	    

	#url(r'^course/form$', views.courseForm, name="CourseForm"),
]