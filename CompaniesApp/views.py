"""
CompaniesApp Views

Created by Jacob Dunbar on 10/2/2016.
"""
from django.shortcuts import render

from . import models

def getCompanies(request):
    companies_list = models.Company.objects.all()
    context = {
        'companies' : companies_list,
        'i' : 1,
    }
    return render(request, 'companies.html', context)

def getCompany(request):
    dict = request.GET
    in_name = dict.get('name', 'None');
    models.Company.objects
    in_description = models.Company.objects.get(name=in_name).description
    context = {
        'name' : in_name,
        'description' : in_description,
    }
    return render(request, 'company.html', context)

def getCompanyForm(request):
	return render(request, 'companyform.html')