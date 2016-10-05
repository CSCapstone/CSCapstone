"""AuthenticationApp Forms

Created by Naman Patwari on 10/4/2016.
"""
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from .models import MyUser

class AdminUserCreationForm(forms.ModelForm):
    """A form for Admin to creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)    

    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'last_name', 'is_student', 'is_professor', 'is_engineer')        

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(AdminUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])         

        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        #fields = ('email', 'password', 'first_name', 'last_name', 'is_active', 'is_admin')
        fields = ('email', 'password', 'first_name', 'last_name', 'is_active', 'is_admin', 
            'is_student', 'is_professor', 'is_engineer')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class LoginForm(forms.Form):
    email = forms.CharField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    """A form to creating new users. Includes all the required
    fields, plus a repeated password."""
    email = forms.CharField(label='Email', widget=forms.EmailInput, required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput, required=True)    

    def clean_password1(self):
        # Return password1
        return self.cleaned_data.get("password1")        

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            exists = MyUser.objects.get(email=email)
            raise forms.ValidationError("This email has already been taken")
        except MyUser.DoesNotExist:
            return email
        except:
            raise forms.ValidationError("There was an error, please contact us later")  


    # firstname = forms.CharField(label="First name", widget=forms.TextInput, required=False)
    # lastname = forms.CharField(label="Last name", widget=forms.TextInput, required=False)

    # student = forms.NullBooleanField(label="Is student?", widget=forms.NullBooleanSelect, required=False)
    # professor = forms.NullBooleanField(label="Is professor?", widget=forms.NullBooleanSelect, required=False)
    # engineer = forms.NullBooleanField(label="Is engineer?", widget=forms.NullBooleanSelect, required=False)         

