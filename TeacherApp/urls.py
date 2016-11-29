from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^teacher/$', views.index, name = "index" ),  # define the homepage for teacherapp
    url(r'^teacherForm/', views.getTeacherForm, name = 'TeacherForm'),   # show the Teacher form to fill out the information for creating a teacher.
    url(r'^submitTeacher/', views.submitTeacher, name = 'submitTeacher'),  # after hitting the submit button on teacher form

]