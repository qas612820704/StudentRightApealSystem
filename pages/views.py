from django.shortcuts import render

from ilt_client.ilt_filter import need_iltlogin
# Create your views here.

def index(request):
    if request.session['user_files']:
        del request.session['user_files']
    return render(request, 'pages/index.html')
