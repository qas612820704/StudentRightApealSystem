from django.http import Http404
from django.shortcuts import render, redirect
from .form import AppealForm, ReplyForm
from .models import Appeal, Reply

# Create your views here.
appeal_identity = {
    'postUser_id' : 'Lego123',
    'name' : 'LegoChiang',
    'department' : 'AM',
    'grade' : 4,
}

def appealNew(request):
    form = AppealForm()
    
    return render(request, 'appeal/appeal_new.html',
                  {'form': form})

def appealNewSubmit(request):
    if request.method == 'POST':
        form = AppealForm(request.POST)
        if form.is_valid():
            try:
                appeal_info = form.cleaned_data
                appeal = Appeal(**appeal_info)
                appeal.postUser_id = appeal_identity['postUser_id']
                appeal.postUser_name = appeal_identity['name']
                appeal.department = appeal_identity['department']
                appeal.grade = appeal_identity['grade']
            except Exception as e:
                print (e)
            appeal.save()
            return redirect('appeal:list')
    else:
        form = AppealForm()
    return render(request, 'appeal/appeal_new.html',
                  {'form': form})

def appealList(request):
    process_status_SemanticUI_style = [('P', 'inverted blue comment icon'), ('D', 'inverted green comment icon'), ('N', 'inverted red comment icon')]
    try:
        appeals = Appeal.objects.all()
    except:
        pass
    return render(request, 'appeal/appeal_list.html', {'appeals' : appeals, 'status_style' : process_status_SemanticUI_style})

def appealDetail(request, pk):
    try:
        appeal = Appeal.objects.get(pk=pk)
    except Appeal.DoesNotExist:
        raise Http404
    reply_form = ReplyForm()

    return render(request, 'appeal/appeal_detail.html', {
        'appeal': appeal,
        'reply_form' : reply_form
        })

def replyNew(request, pk):
    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            reply_info = reply_form.cleaned_data
            reply = Reply(**reply_info)
            reply.postUser_id = appeal_identity['postUser_id']
            reply.postUser_name = appeal_identity['name']
            try:
                appeal = Appeal.objects.get(pk=pk)
            except Appeal.DoesNotExist:
                raise Http404
            reply.appeal = appeal
            reply.save()
            return redirect('appeal:detail', pk=pk)
