from django.conf.urls import patterns, include, url
from django.contrib import admin

from pages import views 

# 4/14 edit by lego
# the big change of the project struct

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'StudentRightAppeal.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^$', views.index, name='home'),
	url(r'^appeal/', include('appeal.urls', namespace='appeal')),
	url(r'^admin/',
		include(admin.site.urls)),
	url(r'^accounts/', include('accounts.urls',namespace='accounts')),
)
