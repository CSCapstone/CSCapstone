"""AuthenticationApp Views

Created by Naman Patwari on 10/4/2016.
"""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages


from .forms import LoginForm, RegisterForm, UpdateForm, UpdateStudent, UpdateTeacher, UpdateEngineer
from .models import MyUser, Student, Teacher, Engineer

from watson import search as watson

# Auth Views

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
			messages.success(request, 'Success! Welcome, '+(user.first_name or ""))
			login(request, user)
			return redirect(next_url)
		else:
			messages.warning(request, 'Invalid username or password.')
			
	context = {
		"form": form,
		"page_name" : "Login",
		"button_value" : "Login",
		"links" : ["register"],
	}
	return render(request, 'auth_form.html', context)

def auth_logout(request):
	logout(request)
	messages.success(request, 'Success, you are now logged out')
	return redirect('home')

@watson.update_index()
def auth_register(request):
	if request.user.is_authenticated():
		return redirect("home")
	
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		new_user = MyUser.objects.create_user(email=form.cleaned_data['email'], 
			password=form.cleaned_data["password2"], 
			first_name=form.cleaned_data['firstname'], last_name=form.cleaned_data['lastname'])
		new_user.save()
		login(request, new_user)

		if form.cleaned_data['acc_type'] == 'S':
			new_student = Student(user = new_user)
			new_student.save()
			return redirect("update_student")
		elif form.cleaned_data['acc_type'] == 'T':
			new_teacher = Teacher(user = new_user)
			new_teacher.save()
			return redirect("update_teacher")
		elif form.cleaned_data['acc_type'] == 'E':
			new_engin = Engineer(user = new_user)
			new_engin.save()
			return redirect("update_engineer")
		
		messages.success(request, 'Success! Your account was created.')
		return render(request, 'index.html')

	context = {
		"form": form,
		"page_name" : "Register",
		"button_value" : "Register",
		"links" : ["login"],
	}
	return render(request, 'auth_form.html', context)

@login_required
@watson.update_index()
def update_profile(request):
	form = UpdateForm(request.POST or None, instance=request.user)
	if form.is_valid():
		form.save()
		messages.success(request, 'Success, your profile was saved!')

	context = {
		"form": form,
		"page_name" : "Update",
		"button_value" : "Update",
		"links" : ["logout"],
	}
	return render(request, 'auth_form.html', context)

@login_required
@watson.update_index()
def update_student(request):
	print request.user.is_teacher
	form = UpdateStudent(request.POST or None, instance=request.user.student)	
	if form.is_valid():				
		form.save()
		return redirect("home")
	context = {
		"form": form,
		"page_name" : "Update",
		"button_value" : "Update",
		"links" : ["logout"],
	}
	return render(request, 'auth_form.html', context)

@login_required
@watson.update_index()
def update_teacher(request):
	form = UpdateTeacher(request.POST or None, instance=request.user.teacher)
	if form.is_valid():
		form.save()
		return redirect("home")
	context = {
		"form": form,
		"page_name" : "Update",
		"button_value" : "Update",
		"links" : ["logout"],
	}
	return render(request, 'auth_form.html', context)

@login_required
@watson.update_index()
def update_engineer(request):
	form = UpdateEngineer(request.POST or None, instance=request.user.engineer)
	if form.is_valid():
		form.save()
		return redirect("home")
	context = {
		"form": form,
		"page_name" : "Update",
		"button_value" : "Update",
		"links" : ["logout"],
	}
	return render(request, 'auth_form.html', context)