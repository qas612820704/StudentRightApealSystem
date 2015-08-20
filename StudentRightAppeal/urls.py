from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from pages import views 
from back_end.views import register, profile

# 4/14 edit by lego
# the big change of the project struct

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'StudentRightAppeal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='home'),
    url(r'^appeal/', include('appeal.urls', namespace='appeal')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ilt_client/', include('ilt_client.urls', namespace='ilt_client')),
    url(r'^backend/', include('back_end.urls', namespace='backend')),
    url(r'^test/', include('mytest.urls', namespace='mytest')),

    url(r'accounts/login/$', login, name='login'),
    url(r'accounts/logout/$', logout, name='logout'),
    url(r'accounts/profile/$', profile, name='profile'),
    url(r'accounts/regist/$', register, name='register'),
)
