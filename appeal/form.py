# 2015/08/06 edit by lego
# 	--BIG CHANGE OF FORM.PY--
# 	Please reference to the MODEL.PY
#
# 2015/06/23 edit by lego
# 	AppealForm add user and department field
#
# 2015/04/19 Create by lego

from django import forms
from base.refrence import GradeChoice, DepartChoice
class AppealGuestForm(forms.Form):
    """ For guest """
    isAuth = False
    title = forms.CharField(
        label='申訴標題',
    	max_length=50)
    context = forms.CharField(
        label='申訴內容',
    	widget=forms.Textarea) 
    name = forms.CharField(
        label='名子',
    	max_length=50)
    sid = forms.CharField(
        label='學號',
        max_length=15)
    department = forms.ChoiceField(
        label='系所',
    	choices=DepartChoice)
    grade = forms.ChoiceField(
        label='年級',
    	choices=GradeChoice)
     
    is_public = forms.BooleanField(
    	label='是否願意讓此成為公開議題?')
    is_public.widget.attrs['disabled'] = True
    is_public.widget.attrs['checked'] = True
class AppealAuthForm(forms.Form):
    """ For Auth """
    isAuth = True;
    title = forms.CharField(max_length=50)
    context = forms.CharField(widget=forms.Textarea)
    is_public = forms.BooleanField(required=False)

class ReplyForm(forms.Form):
	context = forms.CharField()
