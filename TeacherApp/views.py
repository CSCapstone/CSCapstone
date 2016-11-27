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
