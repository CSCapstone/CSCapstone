from django import forms
class TeacherForm(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=120)
    last_name = forms.CharField(label='last_name', max_length=120)
    university = forms.CharField(label='university', max_length=120)
    phone = forms.CharField(label='phone', max_length=10)