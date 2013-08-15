from django.db import models

# Create your models here.
class AidDecline(models.Model):
	name = models.CharField(max_length=50)
	student_id = models.CharField(max_length=7)
	direct_sub = models.BooleanField()
	direct_unsub = models.BooleanField()
	perkins = models.BooleanField()
	work_study = models.BooleanField()
	other1 = models.CharField(max_length=30, null=True, blank=True)
	other2 = models.CharField(max_length=30, null=True, blank=True)
	submit_date = models.DateField(auto_now_add=True)
	def __unicode__(self):
		return self.name
		
class ProxyAidDecline(AidDecline):
	class Meta:
		proxy = True
		app_label = 'Financial_Aid'
		verbose_name = 'Aid Decline Form'

