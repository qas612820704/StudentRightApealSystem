# 2015/08/06 edit by lego
# 	--BIG CHANGE OF FORM.PY--
# 	Please reference to the MODEL.PY
#
# 2015/06/23 edit by lego
# 	AppealForm add user and department field
#
# 2015/04/19 Create by lego

from django import forms
from .refrence import GradeChoice, DepartChoice
class AppealGuestForm(forms.Form):
    """ For guest """
    title = forms.CharField(
    	max_length=50)
    context = forms.CharField(
    	widget=forms.Textarea)
    
    name = forms.CharField(
    	max_length=50)
    department = forms.ChoiceField(
    	choices=DepartChoice)
    grade = forms.ChoiceField(
    	choices=GradeChoice)
    
    is_public = forms.BooleanField(
    	True)
    is_public.widget.attrs['disabled'] = True

class AppealAuthForm(forms.Form):
    """ For Auth """
    title = forms.CharField(max_length=50)
    context = forms.CharField(widget=forms.Textarea)
    is_public = forms.BooleanField(required=False)

class ReplyForm(forms.Form):
	context = forms.CharField()
