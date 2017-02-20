"""
CompaniesApp Views

Created by Jacob Dunbar on 10/2/2016.
"""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from CSCapstone.helpers import redirect_with_param

from . import models
from . import forms

@login_required
def getCompanies(request):
    companies_list = models.Company.objects.all()
    return render(request, 'companies.html', {'companies': companies_list})

@login_required
def getCompany(request):
    in_name = request.GET.get('name', 'None')
    in_company = models.Company.objects.get(name__exact=in_name)
    is_member = False
    if request.user.is_engineer:
        is_member = request.user.engineer.company == in_company
    context = {
        'company' : in_company,
        'userIsMember': is_member,
    }
    return render(request, 'company.html', context)

def getCompanyForm(request):
    if request.method == 'GET':
        return render(request, 'companyform.html')
    elif request.method == 'POST':
        form = forms.CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company_name = form.cleaned_data['name']

            if models.Company.objects.filter(name__exact=company_name).exists():
                return render(request, 'companyform.html', {'error' : 'Error: A company with the name '+company_name+' already exists!'})
            new_company = models.Company(name=company_name, 
                                         photo=request.FILES['photo'],  
                                         description=form.cleaned_data['description'],
                                         website=form.cleaned_data['website'])
            new_company.save()

            return redirect_with_param(request, "company", company_name, 'Success! Created company: '+company_name)

        return render(request, 'companyform.html', {'error' : 'Error: Photo upload failed!'})

def joinCompany(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_company = models.Company.objects.get(name__exact=in_name)
        in_company.members.add(request.user)
        in_company.save();
        request.user.company_set.add(in_company)
        request.user.save()

        return redirect_with_param(request, "company", in_company.name, 'Success! Joined company: '+in_company.name)
    return render(request, 'autherror.html')
    
def unjoinCompany(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_company = models.Company.objects.get(name__exact=in_name)
        in_company.members.remove(request.user)
        in_company.save();
        request.user.company_set.remove(in_company)
        request.user.save()
        
        return redirect_with_param(request, "company", in_company.name, 'Success! Left company: '+in_company.name)
    return render(request, 'autherror.html')
    