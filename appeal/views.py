from django.shortcuts import render, redirect
from .form import AppealForm
# Create your views here.
def appealNew(request):
    form = AppealForm()
    return render(request, 'appeal/appeal_new.html',
                  {'form': form})

def appealNewSubmit(request):
    if request.method == 'POST':
        form = AppealForm(request.POST)
        if form.is_valid():
            return redirect('/')
    else:
        form = AppealForm()
    return render(request, 'appeal/appeal_new.html',
                  {'form': form})
