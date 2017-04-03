"""ProjectsApp Views

Created by Harris Christiansen on 10/02/16.
"""

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from . import forms
from . import models

from watson import search as watson
import itertools

@login_required
def getProjects(request):
	projects_list = models.Project.objects.all()
	project_recomm = models.Project.objects.none()
	if request.user.is_engineer: # Restrict to only engineer's company's projects
		projects_list = request.user.engineer.company.project_set.all()
	elif request.user.is_student: # Recommend projects if Student		
		for tag in request.user.student.tags.all():			
			project_recomm = itertools.chain(watson.filter(models.Project, tag.name),project_recomm)
		project_recomm = set(project_recomm)		
	return render(request, 'projects.html', {'projects': projects_list, 'project_recommended': project_recomm, 'Recommendation':True})

@login_required
def searchProject(request):
	query = request.GET.get('term')	
	if request.user.is_engineer: # Restrict to only engineer's company's projects		
		projects_list = in_university = watson.filter(models.Project.objects.filter(company=request.user.engineer.company), query)		
	else:
		projects_list = in_university = watson.filter(models.Project, query)
	return render(request, 'projects.html', {'projects': projects_list,})	


@login_required
def getProject(request, id):
	project = models.Project.objects.get(id=id)	
	return render(request, 'project.html', { 'project': project })

@login_required
@watson.update_index()
def editProject(request, id=-1):
	if (id == -1): # Create New Project
		project = models.Project(name='')
	else: # Edit Existing Project
		project = models.Project.objects.get(id=id)

	form = forms.ProjectForm(request.POST or None, instance=project) # Validate and update project
	if request.method == 'POST':
		print(request.POST['tags'])
		if form.is_valid():
			if (not project.company and request.user.is_engineer):
				project.company = request.user.engineer.company
			form.save()
			messages.success(request, "Success: Project Saved")
			return redirect('project', project.id)

	return render(request, 'projects-edit.html', { 'project':project, 'form':form })
