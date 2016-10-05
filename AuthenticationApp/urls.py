"""AuthenticationApp URL Configuration

Created by Naman Patwari on 10/4/2016.
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='Home'),
    url(r'^login$', views.login, name='Login'),
    url(r'^logout$', views.logout, name='Logout'),
    url(r'^register$', views.register, name='Register'),    
]