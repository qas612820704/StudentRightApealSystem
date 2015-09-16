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
