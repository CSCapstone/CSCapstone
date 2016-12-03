"""
CompaniesApp Views

Created by Jacob Dunbar on 10/2/2016.
"""
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from . import models
from . import forms

def getCompanies(request):
    if request.user.is_authenticated():
        companies_list = models.Company.objects.all()
        context = {
            'companies' : companies_list,
        }
        return render(request, 'companies.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getCompany(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_company = models.Company.objects.get(name__exact=in_name)
        is_member = in_company.members.filter(email__exact=request.user.email)
        context = {
            'company' : in_company,
            'userIsMember': is_member,
        }
        return render(request, 'company.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getCompanyForm(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = forms.CompanyForm(request.POST, request.FILES)
            context = {
                "form" : form,
                "page_name" : "Create Company",
                "button_value" : "Create"
            }
            if form.is_valid():
                if models.Company.objects.filter(name__exact=form.cleaned_data['name']).exists():
                    messages.error(request,'Error: This company already exists!')
                    return render(request, 'companyform.html', context)
                new_company = models.Company(name=form.cleaned_data['name'],
                                             photo=request.FILES['photo'],
                                             description=form.cleaned_data['description'],
                                             website=form.cleaned_data['website'])
                new_company.save()
                context = {
                    'name' : form.cleaned_data['name'],
                }
                return render(request, 'companyformsuccess.html', context)
            else:
                messages.error(request,'Error: Photo upload failed!')
                return render(request, 'companyform.html', context)
        else:
            form = forms.CompanyForm()
            context = {
                "form" : form,
                "page_name" : "Create Company",
                "button_value" : "Create"
            }
        return render(request, 'companyform.html',context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')


@login_required
def editCompany(request):
    in_name = request.GET.get('name', 'None')
    in_company = models.Company.objects.get(name__exact=in_name)
    form = forms.UpdateCompanyForm(request.POST or None, instance=in_company)
    if form.is_valid():
        form.save()
        messages.success(request, 'Success, this Company is updated!')

    context = {
        "form" : form,
        "page_name" : "Update Company",
        "button_value" : "Update"
    }
    return render(request, 'companyform.html', context)


def joinCompany(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_company = models.Company.objects.get(name__exact=in_name)
        in_company.members.add(request.user)
        in_company.save();
        request.user.company_set.add(in_company)
        request.user.save()
        context = {
            'company' : in_company,
            'userIsMember': True,
        }
        return render(request, 'company.html', context)
    return render(request, 'autherror.html')

def unjoinCompany(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_company = models.Company.objects.get(name__exact=in_name)
        in_company.members.remove(request.user)
        in_company.save();
        request.user.company_set.remove(in_company)
        request.user.save()
        context = {
            'company' : in_company,
            'userIsMember': False,
        }
        return render(request, 'company.html', context)
    return render(request, 'autherror.html')
