"""ProjectsApp Views

Created by Harris Christiansen on 10/02/16.
"""
from django.shortcuts import render

from . import models

def getProjects(request):
	projects_list = models.Project.objects.all()
	return render(request, 'projects.html', {
        'projects': projects_list,
    })

def getProjectForm(request):
	if request.user.is_authenticated():
		if request.user.is_engineer == True:
			return render(request, 'projectform.html')
		return render(request, 'engineerautherror.html')
	return render(request, 'autherror.html')

def getProject(request):
	return render(request, 'project.html')
