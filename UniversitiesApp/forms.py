"""
UniversitiesApp Forms

Created by Jacob Dunbar on 11/5/2016.
"""
from django import forms

from .models import University, Course

class UniversityForm(forms.ModelForm):
    #photo = forms.ImageField(label='Photo')
    name = forms.CharField(min_length=2, label='Name', max_length=50)
    class Meta:
		model = University
		fields = ('name', 'description', 'website', 'photo', 'slug')
	
class CourseForm(forms.ModelForm):
    tag = forms.CharField(label='Tag', max_length=10)
    name = forms.CharField(label='Name', max_length=50)
    description = forms.CharField(label='Description', max_length=300)
    
    class Meta:
        model = Course
        fields = ('tag', 'name', 'description')

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['tag'].widget.attrs.update({
			'placeholder': 'Course Tag',
			'class': 'form-control',
			'data-bvalidator': 'required',
			'data-bvalidator-msg': 'Course Tag Required'
		})
        self.fields['name'].widget.attrs.update({
			'placeholder': 'Course Name',
			'class': 'form-control',
			'data-bvalidator': 'required',
			'data-bvalidator-msg': 'Course Name Required'
		})
        self.fields['description'].widget.attrs.update({
			'placeholder': 'Course Description',
			'class': 'form-control',
			'data-bvalidator': 'required',
			'data-bvalidator-msg': 'Course Description Required'
		})
        
class CourseMemberForm(forms.Form):
    email = forms.CharField(label='Email', max_length=50)