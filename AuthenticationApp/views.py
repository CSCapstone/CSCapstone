"""AuthenticationApp Views

Created by Naman Patwari on 10/4/2016.
"""

from django.shortcuts import render

# Create your views here.

def home(request):		
	context = {
		"user_name": request.user,
	}
	return render(request, 'home.html', context)

def login(request):
	return render(request, 'login.html', {})

def logout(request):
	return render(request, 'logout.html', {})

def register(request):
	return render(request, 'register.html', {})	
