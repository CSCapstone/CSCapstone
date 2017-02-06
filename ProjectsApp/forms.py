"""ProjectsApp Forms

Created by Harris Christiansen on Feb 4, 2017.
"""

from django import forms

from .models import Project

class ProjectForm(forms.ModelForm):
	name = forms.CharField(min_length=2)
	class Meta:
		model = Project
		fields = ('name', 'description')