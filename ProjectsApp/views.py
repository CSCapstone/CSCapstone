"""ProjectsApp Views

Created by Harris Christiansen on 10/02/16.
"""

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from . import forms
from . import models

@login_required
def getProjects(request):
	projects_list = models.Project.objects.all()
	return render(request, 'projects.html', {
        'projects': projects_list,
    })

@login_required
def getProject(request, id):
	project = models.Project.objects.get(id=id)
	return render(request, 'project.html', { 'project': project })

@login_required
def editProject(request, id=-1):
	if (id == -1): # Create New Project
		project = models.Project(name='')
	else: # Edit Existing Project
		project = models.Project.objects.get(id=id)

	form = forms.ProjectForm(request.POST or None, instance=project) # Validate and update project
	if request.method == 'POST':
		if form.is_valid():
			if (not project.company and request.user.is_engineer):
				project.company = request.user.engineer.company
			project.save()
			messages.success(request, "Success: Project Saved")
			return redirect('project', project.id)

	return render(request, 'projects-edit.html', { 'project':project, 'form':form })
