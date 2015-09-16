from django.conf.urls import patterns, url
from appeal import views

urlpatterns = patterns(
    '',
    url(r'^new/$', views.appealNew, name='new'),
    # 4/14 edit by lego
    # Will be done future
    #
    #url(r'^update/$'), views.appealUpdate, name='update'),
    url(r'^(?P<pk>\d+)/$', views.appealDetail, name='detail'),
    url(r'^$', views.appealList, name='list'),
    url(r'^(?P<pk>\d+)/reply/submit/$', views.replyNew, name='replySubmit'),

)
