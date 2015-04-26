from django.conf.urls import patterns, url
from appeal import views

urlpatterns = patterns(
    '',
    url(r'^new/$', views.appealNew, name='new'),
    url(r'^new/submit/$', views.appealNewSubmit, name='newSubmit'),
    # 4/14 edit by lego
    # Will be done future
    #
    #url(r'^$', views.appealIndex, name='index'),
    #url(r'^update/$'), views.appealUpdate, name='update'),
    #url(r'^(?P<pk>\d+)/$', views.appealDetail, name='detail'),

)
