"""GroupsApp Forms

Created by Naman Patwari on 10/10/2016.
"""
from django import forms

class GroupForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    description = forms.CharField(label='Description', max_length=300)
    project = forms.CharField(label='Project', max_length=300)
class GroupAddMemberForm(forms.Form):
    email = forms.CharField(label='email', max_length=30)
    name = forms.CharField(label='name', max_length=30)
