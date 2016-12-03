from django.shortcuts import render

# Create your views here.
from django.contrib import messages

from . import models
from . import forms
from forms import TeacherUpdateForm
from TeacherApp.models import Teacher

def getTeachers(request): 
	if request.user.is_authenticated():
		teachers_list = models.Teacher.objects.all()
		context = {
			'teachers' : teachers_list,
		}

		return render(request, 'teachers.html', context)
	# else
	return render(request, 'autherror.html')

def getTeacher(request):
	if request.user.is_authenticated():
		request_email = request.user.email
		
		try:
			teacher_object = Teacher.objects.get(email=request_email)
			#is_student = teacher_object.students.filter(email__exact=request.user.email)
		except Teacher.DoesNotExist:
			return render(request, 'teacherautherror.html')

		context = {
			'teacher' : teacher_object,
			#'userIsStudent' : is_student,
		}

		return render(request, 'teacher.html', context)

	#else
	return render(request, 'autherror.html')


def getTeacherForm(request):
	if request.user.is_authenticated():
		# Auto Complete name and email from request.user
		return render(request, 'teacherform.html')
	#else
	return render(request, 'autherror.html')

def getTeacherFormSuccess(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			form = forms.TeacherForm(request.POST, request.FILES)
			if form.is_valid():
				if models.Teacher.objects.filter(name__exact=form.cleaned_data['name']).exists():
					return render(request, 'teacherform.html', {'error': 'Error: The teacher name entered already exists!'})
				#else
				new_teacher_object = models.Teacher(name=form.cleaned_data['name'],
								photo=request.FILES['photo'],
								email=form.cleaned_data['email'],
								user_map=request.user,
								)
				new_teacher_object.save()
				
				context = {
					'name': form.cleaned_data['name'],
				}
				
				return render(request, 'teacherformsuccess.html', context)

			else:
				return render(request, 'teacherform.html', {'error': 'Error: Photo upload failed'})
		else:
			form = forms.TeacherForm()
		return render(request, 'teacherform.html')
	return render(request, 'autherror.html')

def updateTeacher(request):
	if request.user.is_authenticated():
	   if request.user.is_professor:
		user_email = request.user.email
		object_teacher = Teacher.objects.get(email=user_email)
		form = TeacherUpdateForm(request.POST or None, instance=object_teacher)#models.Teacher.objects.filter(email=request.user.email))
		
		if form.is_valid():
			form.save()
			messages.success(request, 'Success, your teacher profile was saved!')
		
		context = {
			"form": form,
			"page_name" : "Update Teacher",
			"button_value" : "Update",
			"links" : ["logout"],
		}
		return render(request, 'auth_form.html', context)
	   return render(request, 'teacherautherror.html')	
	return render(request, 'autherror.html') 
