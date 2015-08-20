from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from appeal.models import Appeal, Reply
from back_end.admin import UesrCreationForm
# Create your views here.

import pdb
@login_required
def index(request):
	return render(request, 'backend/index.html')

#def register(request):
#	if request.method == 'POST':
#		form = UesrCreationForm(request.POST)
#		if form.is_valid():
#			user = form.save()
#			return redirect('/')
#		else:
#			form = UesrCreationForm()
#		return render(request, 'back_end/register.html')

def profile(request):
	return render(request, 'accounts/profile.html')

def register(request):
	form = UesrCreationForm()

	return render(request, 'registration/registration_form.html',
		{'form' : form}) 