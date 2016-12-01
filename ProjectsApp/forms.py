from django import forms

class ProjectForm(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    description = forms.CharField(label='Description', max_length=10000)
    programmingLanguage = forms.CharField(label='ProgrammingLanguage', max_length = 200)
    yearsOfExperience = forms.CharField(label='YearsOfExperience')
    speciality = forms.CharField(label='Speciality',max_length=200)