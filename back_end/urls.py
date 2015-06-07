from django.conf.urls import patterns, url
from back_end import views

urlpatterns = patterns(
	'',
	url('^$', views.index, name='index'),
	
)