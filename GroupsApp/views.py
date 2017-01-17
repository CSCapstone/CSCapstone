"""GroupsApp Views
Created by Naman Patwari on 10/10/2016.
"""
from django.shortcuts import render

from . import models
from . import forms

def getGroups(request):
    if request.user.is_authenticated():
        groups_list = models.Group.objects.all()
        context = {
            'groups' : groups_list,
        }
        return render(request, 'groups.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getGroup(request):
	if request.user.is_authenticated():
		in_name = request.GET.get('name', 'None')
		in_group = models.Group.objects.get(name__exact=in_name)
		is_member = in_group.members.filter(email__exact=request.user.email)
		num_requests = in_group.requests.all().count()
		context = {
			'group' : in_group,
			'userIsMember' : is_member,
			'numRequests' : num_requests,
		}
		return render(request, 'group.html', context)
	# render error page if user is not logged in
	return render(request, 'autherror.html')

def getGroupForm(request):
    if request.user.is_authenticated():
        return render(request, 'groupform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getGroupFormSuccess(request):
	if request.user.is_authenticated():
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
				context = {
					'name' : form.cleaned_data['name'],
				}
				return render(request, 'groupformsuccess.html', context)
		else:
			form = forms.GroupForm()
		return render(request, 'groupform.html')
	# render error page if user is not logged in
	return render(request, 'autherror.html')

def getRequests(request):
    if request.user.is_authenticated():
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
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def requestJoinGroup(request):
	if request.user.is_authenticated():
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
		context = {
			'group' : in_group,
			'userIsMember' : False,
			'requestText' : "Request sent",
			'requestColor' : 'green',
		}
		return render(request, 'group.html', context)
	return render(request, 'autherror.html')

def addToGroup(request):
    if request.user.is_authenticated():
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
    return render(request, 'autherror.html')

def removeRequest(request):
	if request.user.is_authenticated():
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
	return render(request, 'autherror.html')

def joinGroup(request):
	if request.user.is_authenticated():
		in_name = request.GET.get('name', 'None')
		in_group = models.Group.objects.get(name__exact=in_name)
		in_group.members.add(request.user)
		in_group.save();
		request.user.group_set.add(in_group)
		request.user.save()
		num_requests = in_group.requests.all().count()
		context = {
			'group' : in_group,
			'userIsMember': True,
			'numRequests' : num_requests,
		}
		return render(request, 'group.html', context)
	return render(request, 'autherror.html')
    
def unjoinGroup(request):
	if request.user.is_authenticated():
		in_name = request.GET.get('name', 'None')
		in_group = models.Group.objects.get(name__exact=in_name)
		in_group.members.remove(request.user)
		in_group.save();
		request.user.requests.remove(in_group)
		request.user.save()
		num_requests = in_group.requests.all().count()
		context = {
			'group' : in_group,
			'userIsMember': False,
			'numRequests' : num_requests,
		}
		return render(request, 'group.html', context)
	return render(request, 'autherror.html')

def addMember(request):
	if request.user.is_authenticated():
		in_name = request.GET.get('name', 'None')
		in_group = models.Group.objects.get(name__exact=in_name)
		if in_group.members.filter(first_name__exact=request.user.first_name, last_name__exact=request.user.last_name).count() > 0:
			context = {
				'group' : in_group,
			}
			return render(request, 'addmember.html', context)
		return render(request, 'accessdenied.html')
	return render(request, 'autherror.html')

def addMemberSuccess(request):
	if request.user.is_authenticated():
		in_name = request.GET.get('name', 'None')
		in_group = models.Group.objects.get(name__exact=in_name)
		if in_group.members.filter(first_name__exact=request.user.first_name, last_name__exact=request.user.last_name).count() > 0:
			if request.method == 'POST':
				form = forms.GroupMemberForm(request.POST)
				if form.is_valid():
					new_member = models.MyUser.objects.get(email__exact=form.cleaned_data['email'])
					if not new_member:
						context = {
							'group' : in_group,
							'error' : 'Error, user does not exist!',
						}
						return render(request, 'addmember.html', context)
					in_group.members.add(new_member)
					in_group.save()
					new_member.members.add(in_group)
					new_member.save()
					is_member = in_group.members.filter(email__exact=request.user.email)
					num_requests = in_group.requests.all().count()
					context = {
						'group' : in_group,
						'userIsMember': is_member,
						'numRequests' : num_requests,
					}
					return render(request, 'group.html', context)
			else:
				form = forms.GroupForm()
			return render(request, 'groupform.html')
		return render(request, 'accessdenied.html')
	return render(request, 'autherror.html')
    