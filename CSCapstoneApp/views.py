"""CSCapstone Views

Created by Harris Christiansen on 9/18/16.
"""

from __future__ import print_function
from django.shortcuts import render
from ProjectsApp.models import Project
from GroupsApp.models import Group
from UniversitiesApp.models import University
from CompaniesApp.models import Company
def getIndex(request):
	projects_list = Project.objects.all()
	groups_list = Group.objects.all()
	universities_list = University.objects.all()
	companies_list = Company.objects.all()
	context = {
		'projects' : projects_list,
		'groups' : groups_list,
		'universities' : universities_list,
		'companies' : companies_list
	}
	return render(request, 'index.html', context)

def getTable(request):
	return render(request, 'table.html')

def getForm(request):
	return render(request, 'form.html')