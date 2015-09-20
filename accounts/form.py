from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from accounts.models import AppealUser

class UesrCreationForm(forms.ModelForm):
  password1 = forms.CharField(
    label = '密碼',
    widget = forms.PasswordInput)
  password2 = forms.CharField(
    label = '密碼驗證',
    widget = forms.PasswordInput)

  class Meta:
    model = AppealUser
    fields = (
      'email',
      'sid',
      'name',
      'nick',
      'department',
      'grade',
    )

  def clean_passwords(self):
    password1 = self.clean_data.get('password1')
    password2 = self.clean_data.get('password2')
    if password1 and password2 and password1 != password2:
      raise forms.ValidationError('passwords don\'t match')
    return password2

  def save(self, commit=True):
    user = super(UesrCreationForm, self).save(commit=False)
    user.set_password(self.cleaned_data['password1'])
    if commit:
      user.save()
    return user

class UserChangeForm(forms.ModelForm):
  password = ReadOnlyPasswordHashField()

  class Meta:
    model = AppealUser
    fields = (
      'name',
      'nick',
      'sid',
      'department',
      'grade',
      'password'
      )

  def clean_password(self):
    return self.initial['password']
