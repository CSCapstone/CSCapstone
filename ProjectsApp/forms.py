from django import forms
from .models import Project

class ProjectForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput, max_length=200,required=False)
    description = forms.CharField(label='Description', widget=forms.Textarea, max_length=10000,required=False)
    programmingLanguage = forms.CharField(label='ProgrammingLanguage', widget=forms.TextInput, max_length = 200,required=False)
    yearsOfExperience = forms.CharField(label='YearsOfExperience', widget=forms.TextInput,required=False)
    speciality = forms.CharField(label='Speciality', widget=forms.TextInput,max_length=200,required=False)

class UpdateForm(forms.ModelForm):

    class Meta:
        model = Project        
        fields = ('name', 'description', 'programmingLanguage', 'yearsOfExperience','speciality')
        widgets = { 
            'description': forms.Textarea()
        }
