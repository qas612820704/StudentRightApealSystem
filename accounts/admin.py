from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from accounts.form import UesrCreationForm, UserChangeForm
from accounts.models import AppealUser,AppealUserManager
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
