"""CSCapstoneApp URL Configuration

Created by Jacob Dunbar on 10/2/2016.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^companies$', views.getCompanies, name='Companies'),
    url(r'^company$', views.getCompany, name='Company'),
    url(r'^companyform$', views.getCompanyForm, name='CompanyForm'),
    url(r'^companyformsuccess$', views.getCompanyFormSuccess, name='CompanyFormSuccess'),
    url(r'^joincompany$', views.joinCompany, name='JoinCompany'),
    url(r'^unjoincompany$', views.unjoinCompany, name='UnjoinCompany'),
]