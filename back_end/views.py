from django.shortcuts import render
from appeal.models import Appeal, Reply
# Create your views here.

def index(request):
	try:
		appeals = Appeal.objects.all()
	except:
		pass
	return render(request, 'appeal/appeal_list.html', {'appeals' : appeals})