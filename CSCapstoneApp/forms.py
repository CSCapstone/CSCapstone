from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms

class TeacherForm(forms.Form):
    image = forms.ImageField(label='Pic', widget=forms.FileInput, required=False)
    university = forms.CharField(label='University', widget=forms.TextInput, required=True)
    department = forms.CharField(label='Department',widget=forms.TextInput, required=True)
    almamater = forms.CharField(label="Alma Mater", widget=forms.TextInput, required=True)
    contact = forms.IntegerField(label='Phone', widget=forms.NumberInput, required=True)