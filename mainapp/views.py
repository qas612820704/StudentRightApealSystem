from django.shortcuts import render
from django.http import HttpRequest

from django.views import generic

# 4/1 edit by lego
# edit class AddView
# add def submitAppeal
# 4/12 edit by lego
# it is become to delete

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'mainapp/index.html'

## command out by lego 04.13 2015
## change addview use the def method
##
# class AddView(generic.TemplateView):
#    template_name = 'mainapp/add.html'
def addappeal(request):
    
    return render(request, 'mainapp/add.html')


def submitAppeal(request):
    pass
