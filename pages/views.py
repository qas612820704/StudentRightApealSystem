from django.shortcuts import render

from ilt_client.ilt_filter import need_iltlogin
# Create your views here.

@need_iltlogin
def index(request):
    return render(request, 'pages/index.html')
