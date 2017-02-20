"""CSCapstone Views

Created by Harris Christiansen on 9/18/16.
"""
from django.shortcuts import render

from UniversitiesApp.models import University
from CompaniesApp.models import Company
from ProjectsApp.models import Project
from GroupsApp.models import Group

def getIndex(request):
	if request.user.is_authenticated():
		num_universities = University.objects.count()
		num_companies = Company.objects.count()
		num_projects = Project.objects.count()
		num_groups = Group.objects.count()
		
		return render(request, 'dashboard.html', {
			'num_universities': num_universities,
			'num_companies': num_companies,
			'num_projects': num_projects,
			'num_groups': num_groups,
		})

	return render(request, 'home.html', {
		'foo': 'bar',
	})