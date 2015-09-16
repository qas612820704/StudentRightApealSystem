from django.shortcuts import render
from accounts.form import UesrCreationForm
# Create your views here.

def profile(request):
  return render(request, 'accounts/profile.html')

def register(request):
  form = UesrCreationForm()
  return render(request, 'registration/registration_form.html',
    {'form':form})
