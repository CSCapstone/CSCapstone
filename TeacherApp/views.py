from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from . import models
from . import forms

def getTeachers(request): 
	if request.user.is_authenticated():
		teachers_list = models.Teacher.objects.all()
		context = {
			'teachers' : teachers_list
		}

		return render(request, 'teachers.html', context)
	# else
	return render(request 'autherror.html')

def getTeacher(request):
	if request.user.is_authenticated():
		request_name = request.GET.get('name', 'None')
		teacher_object = models.Teacher.objects.get(name__exact=request_name)
		is_student = teacher_object.students.filter(email__exact=request.user.email)
		
		context = {
			'teacher' : teacher_object
			'userIsStudent' : is_student
		}

		return render(request, 'teacher.html', context)

	#else
	return render(request, 'autherror.html')


def getTeacherForm(request):
	if request.user.is_authenticated():
		return render(request, 'teacherform.html')
	#else
	return render(request, 'autherror.html')

def getTeacherFormSuccess(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			form = forms.TeacherForm(request.POST, reuest.FILES)
			if form.is_valid():
				if models.Teacher.objects.filter(name__exact=form.cleaned_data['name']).exists():
					return render(request, 'teacherform.html', {'error': 'Error: The teacher name entered already exists!'}}
				#else
				new_teacher_object = models.Teacher(name=form.cleaned_data['name'],
								photo=request.FILES['photo'],
								email=form.cleaned_data['email'],
								university=form.cleaned_data['university'])
				new_teacher.save()
				
				context = {
					'name': form.cleaned_data['name']
				}
				
				return render(request, 'teacherformsuccess.html', context)

			else:
				return render(request, 'teacherform.html', {'error': 'Error: Photo upload failed'})
		else:
			form = forms.TeacherForm()
		return render(request, 'teacherform.html')
	return render(request, 'autherror.html')

