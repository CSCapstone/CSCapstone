from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^comments$', views.getComments, name='Comments'),
]
