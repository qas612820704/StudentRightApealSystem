# 2015/06/23 edit by lego
# AppealForm add user and department field
#
# 2015/04/19 Create by lego

from django import forms

class AppealForm(forms.Form):
    postUser_name = forms.CharField(max_length=50)
    department = forms.CharField(max_length=50)
    title = forms.CharField(max_length=50)
    context = forms.CharField(widget=forms.Textarea)
    is_public = forms.BooleanField(required=False)

class ReplyForm(forms.Form):
	context = forms.CharField()
