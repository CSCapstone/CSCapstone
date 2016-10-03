"""
CompaniesApp Views

Created by Jacob Dunbar on 10/2/2016.
"""
from django.shortcuts import render

from . import models
from . import forms

def getCompanies(request):
    companies_list = models.Company.objects.all()
    context = {
        'companies' : companies_list,
        'i' : 1,
    }
    return render(request, 'companies.html', context)

def getCompany(request):
    in_name = request.GET.get('name', 'None')
    in_company = models.Company.objects.get(name__exact=in_name)
    context = {
        'company' : in_company,
    }
    return render(request, 'company.html', context)

def getCompanyForm(request):
	return render(request, 'companyform.html')

def getCompanyFormSuccess(request):
    if request.method == 'POST':
        form = forms.CompanyForm(request.POST)
        if form.is_valid():
            if models.Company.objects.filter(name__exact=form.cleaned_data['name']).exists():
                return render(request, 'companyform.html', {'error' : 'Error: That company name already exists!'})
            new_company = models.Company(name=form.cleaned_data['name'], description=form.cleaned_data['description'])
            new_company.save()
            context = {
                 'name' : form.cleaned_data['name'],
            }
            return render(request, 'companyformsuccess.html', context)
    else:
        form = forms.CompanyForm()
    
    return render(request, 'companyform.html')