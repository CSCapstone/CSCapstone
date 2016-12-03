from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^teacher/all$', views.getTeachers, name='Teachers'),
	url(r'^teacher/form$', views.getTeacherForm, name='TeacherForm'),
	url(r'^teacher/formsuccess$', views.getTeacherFormSuccess, name='TeacherFormSuccess'),
	url(r'^teacher$', views.getTeacher, name='Teacher'),
	url(r'^teacher/update$', views.updateTeacher, name='UpdateTeacher'),
]
