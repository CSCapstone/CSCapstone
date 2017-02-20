"""GroupsApp Views
Created by Naman Patwari on 10/10/2016.
"""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from CSCapstone.helpers import redirect_with_param

from . import models
from . import forms

@login_required
def getGroups(request):
    groups_list = models.Group.objects.all()
    return render(request, 'groups.html', {'groups' : groups_list})

@login_required
def getGroup(request):
	in_name = request.GET.get('name', 'None')
	in_group = models.Group.objects.get(name__exact=in_name)
	
	is_member = in_group.members.filter(email__exact=request.user.email)
	comments = in_group.comment_set.all()
	num_requests = in_group.requests.all().count()
	context = {
		'group' : in_group,
		'userIsMember' : is_member,
		'numRequests' : num_requests,
		'comments' : comments,
	}
	return render(request, 'group.html', context)

@login_required
def getGroupForm(request):
	if request.method == 'POST':
		form = forms.GroupForm(request.POST)
		if form.is_valid():
			if models.Group.objects.filter(name__exact=form.cleaned_data['name']).exists():
				return render(request, 'groupform.html', {'error' : 'Error: That Group name already exists!'})
			new_group = models.Group(name=form.cleaned_data['name'], description=form.cleaned_data['description'])
			new_group.save()
			new_group.members.add(request.user)
			new_group.save()
			request.user.members.add(new_group)
			request.user.save()

			return redirect_with_param(request, "group", new_group.name, 'Success! Created group: '+new_group.name)
	return render(request, 'groupform.html')

@login_required
def getRequests(request):
	in_name = request.GET.get('name', 'None')
	in_group = models.Group.objects.get(name__exact=in_name)
	if in_group.members.filter(first_name__exact=request.user.first_name, last_name__exact=request.user.last_name).count() > 0:
		# user is authed and a member of the group
		requests_list = in_group.requests.all()
		context = {
			'group' : in_group,
			'requests' : requests_list,
		}
		return render(request, 'requests.html', context)
	# Otherwise access is denied
	return render(request, 'accessdenied.html')

@login_required
def requestJoinGroup(request):
	in_name = request.GET.get('name', 'None')
	in_group = models.Group.objects.get(name__exact=in_name)
	check_requests = in_group.requests.filter(first_name__exact=request.user.first_name)
	check_requests = check_requests.filter(last_name__exact=request.user.last_name)
	if check_requests.count() > 0:
		context = {
			'group' : in_group,
			'userIsMember' : False,
			'requestText' : "Request already sent",
			'requestColor' : 'red'
		}
		return render(request, 'group.html', context)
	in_group.requests.add(request.user)
	in_group.save()
	request.user.requests.add(in_group)
	request.user.save()
	num_requests = in_group.requests.all().count()

	return redirect_with_param(request, "group", in_group.name, 'Success! Request sent to join '+in_group.name)

@login_required
def addToGroup(request):
	in_name = request.GET.get('name', 'None')
	in_group = models.Group.objects.get(name__exact=in_name)
	if in_group.members.filter(first_name__exact=request.user.first_name, last_name__exact=request.user.last_name).count() > 0:
		# user is authed and member of group
		in_email = request.GET.get('email', 'None')
		in_user = models.MyUser.objects.get(email__exact=in_email)
		in_group.members.add(in_user)
		in_group.requests.remove(in_user)
		in_group.save()
		in_user.members.add(in_group)
		in_user.save()
		requests_list = in_group.requests.all()
		context = {
			'group' : in_group,
        	'requests' : requests_list,
		}
		return render(request, 'requests.html', context)
	return render(request, 'accessdenied.html')

@login_required
def removeRequest(request):
	in_name = request.GET.get('name', 'None')
	in_group = models.Group.objects.get(name__exact=in_name)
	if in_group.members.filter(first_name__exact=request.user.first_name, last_name__exact=request.user.last_name).count() > 0:
		# user is authed and member of group
		in_email = request.GET.get('email', 'None')
		in_user = models.MyUser.objects.get(email__exact=in_email)
		in_group.requests.remove(in_user)
		in_group.save()
		in_user.requests.remove(in_group)
		in_user.save()
		requests_list = in_group.requests.all()
		context = {
			'group' : in_group,
        	'requests' : requests_list,
		}
		return render(request, 'requests.html', context)
	return render(request, 'accessdenied.html')

@login_required
def joinGroup(request):
	in_name = request.GET.get('name', 'None')
	in_group = models.Group.objects.get(name__exact=in_name)
	in_group.members.add(request.user)
	in_group.save();
	request.user.group_set.add(in_group)
	request.user.save()

	return redirect_with_param(request, "group", in_group.name, 'Success! Joined group '+in_group.name)
    
@login_required
def unjoinGroup(request):
	in_name = request.GET.get('name', 'None')
	in_group = models.Group.objects.get(name__exact=in_name)
	in_group.members.remove(request.user)
	in_group.save();
	request.user.requests.remove(in_group)
	request.user.save()

	return redirect_with_param(request, "group", in_group.name, 'Success! Left group '+in_group.name)

@login_required
def addMember(request):
	in_name = request.GET.get('name', 'None')
	in_group = models.Group.objects.get(name__exact=in_name)
	if in_group.members.filter(first_name__exact=request.user.first_name, last_name__exact=request.user.last_name).count() > 0:
		context = {
			'group' : in_group,
		}
		return render(request, 'addmember.html', context)
	return render(request, 'accessdenied.html')

@login_required
def addMemberSuccess(request):
	in_name = request.GET.get('name', 'None')
	in_group = models.Group.objects.get(name__exact=in_name)
	if in_group.members.filter(first_name__exact=request.user.first_name, last_name__exact=request.user.last_name).count() > 0:
		if request.method == 'POST':
			form = forms.GroupMemberForm(request.POST)
			if form.is_valid():
				new_member = models.MyUser.objects.filter(email__exact=form.cleaned_data['email']).first()
				if not new_member:
					context = {
						'group' : in_group,
						'error' : 'Error, user does not exist!',
					}
					return render(request, 'addmember.html', context)
				in_group.members.add(new_member)
				in_group.requests.remove(new_member)
				in_group.save()
				new_member.members.add(in_group)
				new_member.save()
				return redirect_with_param(request, "group", in_group.name, 'Success! Added '+new_member.name+' to group '+in_group.name)
		else:
			form = forms.GroupForm()
		return render(request, 'groupform.html')
	return render(request, 'accessdenied.html')

@login_required
def addComment(request):
	in_name = request.GET.get('name', 'None')
	in_group = models.Group.objects.get(name__exact=in_name)
	if in_group.members.filter(first_name__exact=request.user.first_name, last_name__exact=request.user.last_name).count() > 0:
		if request.method == 'POST':
			form = forms.CommentForm(request.POST)
			if form.is_valid():
				new_comment = models.Comment(poster=request.user, group=in_group, text=form.cleaned_data['comment'])
				new_comment.save()
				return redirect_with_param(request, "group", in_group.name, 'Success! Added comment to group: '+in_group.name)
		else:
			form = forms.GroupForm()
		return render(request, 'groupform.html')
	return render(request, 'accessdenied.html')

@login_required
def deleteComment(request):
	in_name = request.GET.get('name', 'None')
	in_group = models.Group.objects.get(name__exact=in_name)
	if in_group.members.filter(first_name__exact=request.user.first_name, last_name__exact=request.user.last_name):
		cid = request.GET.get('cid', 'None')
		comment = request.user.comment_set.filter(cid__exact=cid)
		comment.delete()

		return redirect_with_param(request, "group", in_group.name, 'Success! Deleted comment from group: '+in_group.name)
	return render(request, 'accessdenied.html')

