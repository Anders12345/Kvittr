from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^$', include('theme.urls')),
	url(r'^useraccounts/', include('useraccounts.urls')),
	url(r'^kvittrmsg/', include('kvittrmsg.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
