from django.shortcuts import render

# Create your views here.

def profile(request):
  return render(request, 'accounts/profile.html')

def register(request):
  form = UesrCreationForm()

  return render(request, 'registration/registration_form.html',
    {'form' : form})

#def register(request):
# if request.method == 'POST':
#   form = UesrCreationForm(request.POST)
#   if form.is_valid():
#     user = form.save()
#     return redirect('/')
#   else:
#     form = UesrCreationForm()
#   return render(request, 'back_end/register.html')
