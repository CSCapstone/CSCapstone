"""CSCapstone Views

Created by Harris Christiansen on 9/18/16.
"""
from django.shortcuts import render

def index(request):
	return render(request, 'index.html', {
        'foo': 'bar',
    })
