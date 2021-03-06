from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from back_end.models import AppealUser

class UesrCreationForm(forms.ModelForm):
	password1 = forms.CharField(
		label = 'Password',
		widget = forms.PasswordInput)
	password2 = forms.CharField(
		label = 'Password Confirmation',
		widget = forms.PasswordInput)

	class Meta:
		model = AppealUser
		fields = (
			'email',
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
			'password',
			'name',
			'nick',
			'department',
			'grade',
			'is_active',
			'is_admin')

	def clean_password(self):
		return self.initial['password']

class AppealUserAdmin(UserAdmin):
	form = UserChangeForm
	add_form = UesrCreationForm

	list_display = (
		'email',
		'name',
		'nick',
		'department',
		'grade',
		'date_of_birth',
		'is_admin'
	)
	list_filter = (
		'is_admin',
	)
	fieldsets = ( 
		(None, {'fields': ('email', 'password')}),
		('Personal info', {'fields': (
			'name',
			'nick',
			'department',
			'grade',)}),
		('Permissions', {'fields': (
			'is_admin',)}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': (
				'email',
				'name',
				'nick',
				'department',
				'grade', 
				'password1', 
				'password2')}
		),
	)
	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ()

admin.site.register(AppealUser, AppealUserAdmin)
admin.site.unregister(Group)