"""GroupsApp URL

Created by Naman Patwari on 10/10/2016.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^group/all$', views.getGroups, name='Groups'),
	url(r'^group/form$', views.getGroupForm, name='GroupForm'),
    url(r'^group/formsuccess$', views.getGroupFormSuccess, name='GroupFormSuccess'),
	url(r'^group/requestjoin$', views.requestJoinGroup, name='RequestJoinGroup'),
	url(r'^group/requests$', views.getRequests, name='Requests'),
	url(r'^group/addtogroup$', views.addToGroup, name='AddToGroup'),
	url(r'^group/removerequest$', views.removeRequest, name='RemoveRequest'),
    url(r'^group/join$', views.joinGroup, name='GJoin'),
    url(r'^group/unjoin$', views.unjoinGroup, name='GUnjoin'),
    url(r'^group$', views.getGroup, name='Group'),
	url(r'^group/addmember$', views.addMember, name='AddMember'),
	url(r'^group/addmembersuccess$', views.addMemberSuccess, name='AddMemberSuccess'),
	url(r'^group/addcomment$', views.addComment, name='AddComment'),
	url(r'^group/deletecomment$', views.deleteComment, name='DeleteComment'),
]