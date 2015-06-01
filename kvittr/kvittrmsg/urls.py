from django.conf.urls import patterns, url

from kvittrmsg import views

urlpatterns = patterns('',
	url(r'^$', views.list_msgs, name='list_msgs'),
	url(r'^(\d+)/$', views.msg_details, name='msg_details'),
	url(r'^(\d+)/add_likes/(\d+)$', views.msg_add_likes, name='msg_add_likes'),
)