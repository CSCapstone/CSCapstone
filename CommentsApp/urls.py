
from django.conf.urls import url
from . import views

app_name = 'comment'

urlpatterns = [
    #url(r'^viewComment/$', views.getComments, name='Comments'),
    url(r'^$', views.getComments, name='Comments'),
    url(r'^getCommentForm/$', views.getCommentForm, name='CommentForm'),
    url(r'^addComment/$', views.addComment, name='AddComment'),
    url(r'^addSubComment/(?P<comment_id>[0-9]+)/$', views.addSubComment, name='addSubComment'),
]
