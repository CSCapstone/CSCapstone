"""
CompaniesApp Forms

Created by Jacob Dunbar on 10/3/2016.
"""
from django import forms
from .models import Company
class CompanyForm(forms.Form):
    name = forms.CharField(label='Name',widget=forms.TextInput,required=True)
    photo = forms.ImageField(label='Photo',required=True)
    description = forms.CharField(label='Description',widget=forms.Textarea, required=False,initial='/')
    website = forms.CharField(label='Website', widget=forms.TextInput,required=False,initial='/')

class UpdateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'photo', 'description','website')
        widgets = {
            'description': forms.Textarea()
        }
    def __init__(self, *args, **kwargs):

         #init the form as usual
         super(UpdateCompanyForm, self).__init__(*args, **kwargs)

         #then change the required status on the fields:
         self.fields['photo'].required = False
         self.fields['website'].required = False
         self.fields['description'].required = False
