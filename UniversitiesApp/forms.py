"""
UniversitiesApp Forms

Created by Jacob Dunbar on 11/5/2016.
"""
from django import forms

from .models import University

class UniversityForm(forms.ModelForm):
    #photo = forms.ImageField(label='Photo')
    name = forms.CharField(min_length=2, label='Name', max_length=50)
    class Meta:
		model = University
		fields = ('name', 'description', 'website', 'photo', 'slug')
	
class CourseForm(forms.Form):
	tag = forms.CharField(label='Tag', max_length=10)
	name = forms.CharField(label='Name', max_length=50)
	description = forms.CharField(label='Description', max_length=300)