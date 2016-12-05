from django import forms

from models import MyUser, Teacher

class TeacherForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50, widget=forms.TextInput, required=True)
    photo = forms.ImageField(label='Photo')
    email = forms.CharField(label='Email', max_length=300, widget=forms.EmailInput, required=True)

class TeacherUpdateForm(forms.ModelForm):
    class Meta:
	model = Teacher
	fields = ('name', 'photo', 'email')

    def clean_email(self):
	email=self.cleaned_data.get("email")
	
	if email == self.initial["email"]:
		return email

	try:
		exists = MyUser.objects.get(email=email)
		raise forms.ValidationError("This email has already been taken")
	except MyUser.DoesNotExist:
		return email
