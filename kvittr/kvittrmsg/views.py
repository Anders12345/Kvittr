from django.shortcuts import render
from django.utils import timezone

from kvittrmsg.models import Kvittrmsg

def list_msgs(request):
	if request.method == 'POST':
		new_msg_text = request.POST.get('new_msg')
		new_msg = Kvittrmsg()
		new_msg.msg = new_msg_text
		new_msg.created_datetime = timezone.now()
		new_msg.created_by = request.user
		new_msg.save()

	msgs = Kvittrmsg.objects.all()

	context = {'msgs': msgs}
	return render(request, 'kvittrmsg/list_msgs.html', context)

