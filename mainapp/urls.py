from django.conf.urls import patterns, include, url
from django.contrib import admin
from mainapp import views
urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
)
 
