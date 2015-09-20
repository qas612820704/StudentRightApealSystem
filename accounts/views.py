from django.shortcuts import render, redirect
from accounts.form import UesrCreationForm,UserChangeForm
from accounts.models import AppealUser
# Create your views here.

def profile(request):
  try:
    user = AppealUser.objects.get(pk=request.user.pk)
  except Exception as e:
    raise e
  return render(request, 'accounts/profile.html',
  {'user':user})

def register(request):
  if request.method == 'GET':
    form = UesrCreationForm()
    return render(request, 'registration/registration_form.html',
    {'form':form})
  elif request.method == 'POST':
    form = UesrCreationForm(request.POST)

    if form.is_valid():
      try:
        user = form.save()
      except Exception as e:
        raise e
      return redirect('accounts:login')
    return render(request, 'registration/registration_form.html',
    {'form':form})
