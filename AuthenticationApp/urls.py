"""AuthenticationApp URL Configuration

Created by Naman Patwari on 10/4/2016.
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login$', views.auth_login, name='login'),
    url(r'^logout$', views.auth_logout, name='logout'),
    url(r'^register$', views.auth_register, name='register'),
    url(r'^update$', views.update_profile, name='update_profile'),   
    url(r'^student/updateProfile$', views.update_student, name='update_student'),   
    url(r'^teacher/updateProfile$', views.update_teacher, name='update_teacher'),   
    url(r'^engineer/updateProfile$', views.update_engineer, name='update_engineer'),   
]