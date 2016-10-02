"""ProjectsApp Views

Created by Harris Christiansen on 10/02/16.
"""
from django.shortcuts import render

def getProjects(request):
	return render(request, 'projects.html')

def getProject(request):
	return render(request, 'project.html')
