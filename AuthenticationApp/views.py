"""AuthenticationApp Views

Created by Naman Patwari on 10/4/2016.
"""

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


from .forms import LoginForm, RegisterForm
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
		email = form.cleaned_data['email']
		password = form.cleaned_data["password2"]
		new_user = MyUser.objects.create_user(email=email, password=password)
		new_user.save()
		login(request, new_user)
		return HttpResponseRedirect("/")

	context = {"form": form,}
	return render(request, 'register.html', context)


	# email = form.cleaned_data['email']
 #    password1 = form.cleaned_data['password1']
 #    password2 = form.cleaned_data['email']
 
 #    firstname = form.cleaned_data['firstname'] lastname =
 #    form.cleaned_data['lastname']

 #    student = form.cleaned_data['student']
 #    professor = form.cleaned_data['professor']
 #    engineer = form.cleaned_data['engineer']

    # email = forms.CharField(label='Email', widget=forms.EmailInput)
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)    
    
    # firstname = forms.CharField(label="First name", widget=forms.TextInput)
    # lastname = forms.CharField(label="Last name", widget=forms.TextInput)

    # student = forms.NullBooleanField(label="Is student?", widget=forms.NullBooleanSelect)
    # professor = forms.NullBooleanField(label="Is professor?", widget=forms.NullBooleanSelect)
    # engineer = forms.NullBooleanField(label="Is engineer?", widget=forms.NullBooleanSelect) 