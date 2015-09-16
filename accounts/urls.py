from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from accounts import views

urlpatterns = patterns(
  '',
  url(r'^login/$', login, name='login'),
  url(r'^logout/$', logout, name='logout'),
  url(r'^profile/$', views.profile, name='profile'),
  url(r'^register/$', views.register, name='register'),
)
