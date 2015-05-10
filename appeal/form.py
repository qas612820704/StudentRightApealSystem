# add form.py by lego 2015/04/19

from django import forms

class AppealForm(forms.Form):
    title = forms.CharField(max_length=50)
    context = forms.CharField(widget=forms.Textarea)
    is_public = forms.BooleanField(required=False)

class ReplyForm(forms.Form):
	context = forms.CharField()
