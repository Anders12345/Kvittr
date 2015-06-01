from django.db import models
from django.contrib.auth.models import User

class Kvittrmsg(models.Model):
	msg = models.TextField()
	created_datetime = models.DateTimeField()
	created_by = models.ForeignKey(User, related_name='created_msg')
	likes = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return u'%s' % self.msg

	class Meta:
		ordering = ['-id']
