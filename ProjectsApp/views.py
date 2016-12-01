"""ProjectsApp Views

Created by Harris Christiansen on 10/02/16.
"""
from django.shortcuts import render

from . import models
from . import forms
import datetime

def getProjects(request):
	projects_list = models.Project.objects.all()
	return render(request, 'projects.html', {
        'projects': projects_list,
    })

def getProject(request):
	in_name = request.GET.get('name', 'None')
	in_project = models.Project.objects.get(name__exact=in_name)
	is_member = in_project.createdBy.filter(email__exact=request.user.email)
	is_engineer = request.user.is_engineer
	context = {
		'project' : in_project,
		'userIsMember': is_member,
		'is_engineer' : is_engineer
	}
	return render(request, 'project.html',context)

def getProjectForm(request):
	if request.user.is_authenticated():
		return render(request,'projectform.html')
	return render(request,'autherror.html')

def getProjectFormSuccess(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = forms.ProjectForm(request.POST)
            if form.is_valid():
                if models.Project.objects.filter(name__exact=form.cleaned_data['name']).exists():
                    return render(request, 'projectform.html', {'error' : 'Error: That Project name already exists!'})
                new_project = models.Project(name=form.cleaned_data['name'], description=form.cleaned_data['description'],programmingLanguage=form.cleaned_data['programmingLanguage'],yearsOfExperience=form.cleaned_data['yearsOfExperience'],speciality=form.cleaned_data['speciality'])
                new_project.created_at = datetime.datetime.now()
                new_project.updated_at = datetime.datetime.now()

                new_project.save()
                new_project.createdBy.add(request.user)
                # request.user.projects_set.add(new_project)
                new_project.save()
                request.user.save()
                context = {
                    'name' : form.cleaned_data['name'],
                }
                return render(request, 'projectformsuccess.html', context)
        else:
            form = forms.ProjectForm()
        return render(request, 'projectform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

