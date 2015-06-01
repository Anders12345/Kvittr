from django.conf.urls import patterns, url

from kvittrmsg import views

urlpatterns = patterns('',
	url(r'^$', views.list_msgs, name='list_msgs'),
)