"""
CompaniesApp Views

Created by Jacob Dunbar on 10/2/2016.
"""
from django.shortcuts import render

def getCompanies(request):
	return render(request, 'companies.html', {
        'foo': 'bar',
    })

def getCompany(request):
	return render(request, 'company.html')

def getCompanyForm(request):
	return render(request, 'companyform.html')