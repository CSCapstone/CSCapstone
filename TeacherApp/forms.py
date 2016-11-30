from django import forms

class TeacherForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50, widget=forms.TextInput, required=True)
    photo = forms.ImageField(label='Photo')
    email = forms.CharField(label='Email', max_length=300, widget=forms.EmailInput, required=True)
    university = forms.CharField(label='University', max_length = 300, widget=forms.TextInput, required=False)
