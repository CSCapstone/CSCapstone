"""CompaniesApp URL Configuration

Created by Jacob Dunbar on 10/2/2016.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^company/all$', views.getCompanies, name='companies'),
	url(r'^company/form$', views.getCompanyForm, name='company_form'),
    url(r'^company/join$', views.joinCompany, name='company_join'),
    url(r'^company/unjoin$', views.unjoinCompany, name='company_unjoin'),
    url(r'^company', views.getCompany, name='company'),
]