"""GroupsApp URL

Created by Naman Patwari on 10/10/2016.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^group/all$', views.getGroups, name='groups'),
	url(r'^group/form$', views.getGroupForm, name='group_form'),
	url(r'^group/requestjoin$', views.requestJoinGroup, name='group_request'),
	url(r'^group/requests$', views.getRequests, name='group_requests'),
	url(r'^group/addtogroup$', views.addToGroup, name='group_add'),
	url(r'^group/removerequest$', views.removeRequest, name='group_reject'),
    url(r'^group/join$', views.joinGroup, name='group_join'),
    url(r'^group/unjoin$', views.unjoinGroup, name='group_unjoin'),
    url(r'^group$', views.getGroup, name='group'),
	url(r'^group/addmember$', views.addMember, name='group_add'),
	url(r'^group/addcomment$', views.addComment, name='group_comment'),
	url(r'^group/deletecomment$', views.deleteComment, name='group_comment_delete'),
]