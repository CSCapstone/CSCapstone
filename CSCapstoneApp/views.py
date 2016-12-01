"""CSCapstone Views

Created by Harris Christiansen on 9/18/16.
"""
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages


from .forms import TeacherForm

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

def profile_edit(request):
    current_user = request.user

    if current_user.is_professor == True:
        form = TeacherForm(request.POST or None)
    #elif
        #TODO


    next_url = request.GET.get('next')
    if next_url is None:
        next_url = "/home"

    if form.is_valid():
        if current_user.is_professor == True:
            university = form.cleaned_data['university']
            department = form.cleaned_data['department']
            contact = form.cleaned_data['contact']
            almamater = form.cleaned_data['almamater']
            image = form.data['image']
            t = Teacher.objects.filter(teacher=request.user)[0]
            t.university = university
            t.department = department
            t.contact = contact
            t.pic = image
            t.almamater = almamater
            t.save()

        if current_user is not None:
            messages.success(request, 'Success! Updated')
            return HttpResponseRedirect(next_url)
        else:
            messages.warning(request, 'Something went wrong!')

    context = {
        "form": form,
        "page_name": "Update Your Profile Info",
        "button_value": "Update",
        "links": ["Home"],
    }
    return render(request, 'update.html', context)