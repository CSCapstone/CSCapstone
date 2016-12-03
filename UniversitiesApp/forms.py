"""
UniversitiesApp Forms

Created by Jacob Dunbar on 11/5/2016.
"""
from django import forms
from .models import University, Course

class UniversityForm(forms.Form):
    name = forms.CharField(label='Name',widget=forms.TextInput,required=True)
    photo = forms.ImageField(label='Photo',required=False)
    description = forms.CharField(label='Description',widget=forms.Textarea, required=False)
    website = forms.CharField(label='Website', widget=forms.TextInput,required=False)


class UpdateUniversityForm(forms.ModelForm):

    class Meta:
        model = University
        fields = ('name', 'photo', 'description','website')
        widgets = {
            'description': forms.Textarea()
        }

class CourseForm(forms.Form):
    tag = forms.CharField(label='Tag (ex. CS490)', widget=forms.TextInput, max_length=10,required=True)
    name = forms.CharField(label='Name (ex. Senior Design)', widget=forms.TextInput, max_length=50,required=True)
    description = forms.CharField(label='Description',widget=forms.Textarea, max_length=300,required=False)

class UpdateCourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('tag', 'name', 'description')
        widgets = {
            'description': forms.Textarea()
        }
