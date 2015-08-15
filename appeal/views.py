from django.http import Http404
from django.shortcuts import render, redirect
from .form import AppealGuestForm, ReplyForm
from .models import Appeal, Reply
from subprocess import call
# Create your views here.

def appealNew(request):
    form = AppealGuestForm()
    
    return render(request, 'appeal/appeal_new.html',
                  {'form': form})

def appealNewSubmit(request):
    if request.method == 'POST':
        form = AppealGuestForm(request.POST)
        if form.is_valid():
            try:
                appeal_info = form.cleaned_data
                appeal = Appeal(**appeal_info)
                appeal.save()
            except Exception as e:
                print (e)
            return redirect('appeal:list')
    else:
        form = AppealGuestForm()
    return render(request, 'appeal/appeal_new.html',
                  {'form': form})

def appealList(request):
    process_status_SemanticUI_style = [('P', 'inverted blue comment icon'), ('D', 'inverted green comment icon'), ('N', 'inverted red comment icon')]
    content = {}
    try:
        appeals = Appeal.objects.all()
        content['appeals'] = appeals
        if 'userInfo' in request.session:
            identity = request.session['userInfo']
            content['identity'] = identity
    except Exception as e:
        call(["xcowsay", repr(e)])
        raise e
    return render(request, 'appeal/appeal_list.html', {
            'content' : content,
            }
        )

def appealDetail(request, pk):
    content = {}
    if 'userInfo' in request.session:
            identity = request.session['userInfo']
            content['identity'] = identity
    try:
        content['appeal'] = Appeal.objects.get(pk=pk)
    except Appeal.DoesNotExist:
        raise Http404
    content['reply_form'] = ReplyForm()

    return render(request, 'appeal/appeal_detail.html', {
        'content': content,
        })

def replyNew(request, pk):
    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            reply_info = reply_form.cleaned_data
            reply = Reply(**reply_info)
            reply.name = request.session['userInfo']['data']['info']['first_name']
            reply.username = request.session['userInfo']['data']['info']['username']
            try:
                appeal = Appeal.objects.get(pk=pk)
            except Appeal.DoesNotExist:
                raise Http404
            reply.appeal = appeal
            reply.save()
            return redirect('appeal:detail', pk=pk)
