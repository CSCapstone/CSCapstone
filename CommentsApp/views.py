from django.shortcuts import render

# Create your views here.
from . import models
#from . import forms

# Create your views here.
def getComments(request):
    return render(request, 'comments.html')

