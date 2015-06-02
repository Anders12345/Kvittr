from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

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
	
	paginator = Paginator(msgs, 5)
	
	page = request.GET.get('page')
	
	try:
		msgs = paginator.page(page)
	except PageNotAnInteger:
		msgs = paginator.page(1)
	except EmptyPage:
		msgs = paginator.page(paginator.num_pages)
	
	context = {'msgs': msgs}
	return render(request, 'kvittrmsg/list_msgs.html', context)

def msg_details(request, id):
	msg = Kvittrmsg.objects.get(pk=id)
	context = {'msg': msg}
	return render(request, 'kvittrmsg/msg_details.html', context)

def msg_add_likes(request, id1, id):
	msg = Kvittrmsg.objects.get(pk=id)
	msg.likes = msg.likes + 1
	msg.save()
	data = {'likes_updated': msg.likes}
	return JsonResponse(data)