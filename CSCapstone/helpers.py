"""CSCapstone Project: Helpers
File created by Harris Christiansen on February 20, 2017
"""

from django.contrib import messages
from django.shortcuts import redirect

def redirect_with_param(request, page, param, alert=""):
	if alert!="":
		messages.success(request, alert)
	response = redirect(page)
	response['Location'] += "?name="+param
	return response