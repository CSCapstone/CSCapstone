"""AuthenticationApp Views

Created by Naman Patwari on 10/4/2016.
"""

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


from .forms import LoginForm, RegisterForm, UpdateForm
from .models import MyUser

# Create your views here.

@login_required
def home(request):	
	context = {"user_name": request.user.first_name,}
	return render(request, 'home.html', context)

def auth_login(request):
	form = LoginForm(request.POST or None)
	next_url = request.GET.get('next')
	if next_url is None:
		next_url = "/"
	if form.is_valid():
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']
		user = authenticate(email=email, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(next_url)
			
	context = {
		"form" : form
	}
	return render(request, 'login.html', context)

def auth_logout(request):
	logout(request);
	return HttpResponseRedirect("/")

def auth_register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/")
	
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		new_user = MyUser.objects.create_user(email=form.cleaned_data['email'], 
			password=form.cleaned_data["password2"], 
			first_name=form.cleaned_data['firstname'], last_name=form.cleaned_data['lastname'],
    		is_student=form.cleaned_data['student'], is_professor=form.cleaned_data['professor'], 
    		is_engineer=form.cleaned_data['engineer'])
		new_user.save()		
		return HttpResponseRedirect("/login")

	context = {"form": form,}
	return render(request, 'register.html', context)

def update_profile(request):
	#TODO : Make new form and start editing information
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/")

	form = UpdateForm(request.POST or None, instance=request.user)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/")

	context = {"form": form,}
	return render(request, 'register.html', context)
