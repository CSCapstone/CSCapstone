"""AuthenticationApp Forms

Created by Naman Patwari on 10/4/2016.
"""
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from django.db import models

from .models import Project
#from ...CompaniesApp.models import Company

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'company',
            'language',
            'experience',
            'speciality'
        ]
        labels = {
            'experience' : 'Years of Experience'
        }
    # name = forms.CharField(label='Project Name', widget=forms.TextInput, required=True)
    # description = forms.CharField(label='Project Description', widget=forms.TextInput, required=True)
    # company = forms.ModelMultipleChoiceField(queryset=companies_model.) 
    # #models.ForeignKey("CompaniesApp.Company", related_name="company")
    # language = forms.CharField(label='Language(s)', widget=forms.TextInput, required=False)
    # experience = forms.CharField(label='Years of Experience', widget=forms.TextInput, required=False)
    # speciality = forms.CharField(label='Speciality', widget=forms.TextInput, required=False)