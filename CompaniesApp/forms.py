from django import forms

class CompanyForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    description = forms.CharField(label='Description', max_length=300)