"""ProjectsApp Forms

File created by Harris Christiansen on Feb 4, 2017.
"""

from django import forms

from .models import Project

class ProjectForm(forms.ModelForm):
	name = forms.CharField(label="Project Name", min_length=2)
	description = forms.CharField(label="Project Description", min_length=10)

	class Meta:
		model = Project
		fields = ('name', 'description', 'tags')

	def __init__(self, *args, **kwargs):
		super(ProjectForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({
			'placeholder': 'Project Name',
			'class': 'form-control',
			'data-bvalidator': 'required',
			'data-bvalidator-msg': 'Project Name Required'
		})
		self.fields['description'].widget.attrs.update({
			'placeholder': 'Project Description',
			'class': 'form-control',
			'data-bvalidator': 'required',
			'data-bvalidator-msg': 'Project Description Required'
		})
		self.fields['tags'].widget.attrs.update({
			'class': 'tagSelect',
			'style': 'width: 100%;',
			'data-bvalidator': 'required',
			'data-bvalidator-msg': 'Please select at least 1 tag.'
		})

	def clean_tags(self):
		print(" !!!!! HERE !!!!! ")
		tags = self.cleaned_data.get("tags")
		print tags
		return tags
