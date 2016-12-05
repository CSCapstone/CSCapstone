from django import forms
class CommentForm(forms.Form):
    comment = forms.CharField(label='Text', max_length=500)
