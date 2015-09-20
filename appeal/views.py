from django.http import Http404
from django.shortcuts import render, redirect
from .form import AppealGuestForm, AppealAuthForm,ReplyForm,AppealPowerForm
from .models import Appeal, Reply
from subprocess import call
# Create your views here.


def appealNew(request):
	if request.method == 'GET':
		if request.user.is_authenticated():
			form = AppealAuthForm()
		else:
			form = AppealGuestForm()
		return render(request, 'appeal/appeal_new.html',{'form': form})
	elif request.method == 'POST':
		if request.user.is_authenticated():
			form = AppealAuthForm(request.POST)
		else:
			form = AppealGuestForm(request.POST)
		if form.is_valid():
			try:
				appeal_info = form.cleaned_data
				appeal = Appeal(**appeal_info)
				if request.user.is_authenticated():
					appeal.username = request.user
				appeal.save()
			except Exception as e:
				print (e)
			return redirect('appeal:list')
		return render(request, 'appeal/appeal_new.html',{'form': form})

def appealList(request):
	content = {}
	if request.user.is_authenticated() and request.user.is_admin:
		try:
			appeals = Appeal.objects.order_by('-pub_date')
			content['appeals'] = appeals
		except Exception as e:
			raise e
	else:
		try:
			appeals = Appeal.objects.filter(is_public=True).order_by('-pub_date')
			content['appeals'] = appeals
		except Exception as e:
			raise e
	return render(request, 'appeal/appeal_list.html', {
			'content' : content,
			}
		)

def appealDetail(request, pk):
	try:
		appeal = Appeal.objects.get(pk=pk)
	except Appeal.DoesNotExist:
		raise Http404
	if request.method == 'GET':
		rForm = ReplyForm()
		pForm = AppealPowerForm()
		return render(request, 'appeal/appeal_detail.html', {
			'appeal': appeal,
			'rForm': rForm,
			'pForm': pForm,
			})
	elif request.method	== 'POST':
		pForm = AppealPowerForm(request.POST, instance=appeal)
		if pForm.is_valid():
			pForm.save()
		return redirect('appeal:detail',pk)


def replyNew(request, pk):
	if request.method == 'POST':
		form = ReplyForm(request.POST)
		if form.is_valid():
			info = form.cleaned_data
			reply = Reply(**info)
			reply.username = request.user
			try:
				reply.appeal = Appeal.objects.get(pk=pk)
				reply.save()
			except Appeal.DoesNotExist:
				raise Http404
			return redirect('appeal:detail', pk=pk)
		else:
			raise Http404
