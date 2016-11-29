"""CSCapstone Views

Created by Harris Christiansen on 9/18/16.
"""
from django.shortcuts import render
from AuthenticationApp.models import Teacher

def getIndex(request):
	return render(request, 'index.html', {
        'foo': 'bar',
    })

def getTable(request):
	return render(request, 'table.html')

def getForm(request):
	return render(request, 'form.html')

def getHome(request):
	if request.user.is_professor == True:
		type = "Teacher"
		a = Teacher.objects.filter(teacher=request.user)[0]

	return render(request, 'home.html',{
		'profile': a,
		'user': request.user,
		'type': type
    })