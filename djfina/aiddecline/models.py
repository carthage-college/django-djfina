from django.db import models

# Create your models here.
class AidDeclineModel(models.Model):
    
    #Fields in the forms are down below
	name = models.CharField(max_length=50)
	student_id = models.CharField(max_length=7)
	direct_sub = models.BooleanField() #Renders as a checkbox
	direct_unsub = models.BooleanField()
	perkins = models.BooleanField()
	work_study = models.BooleanField()
	other1 = models.CharField(max_length=30, null=True, blank=True) #'null=True' can be represented as null in the database
	other2 = models.CharField(max_length=30, null=True, blank=True) #'blank=True', this field can be left blank
	submit_date = models.DateField(auto_now_add=True) #Automatically adds the current date and is invisible on the form
	
	#How the class is represented in the admin page
	def __unicode__(self):
		return self.name
		
    class Meta:
        verbose_name = 'Aid decline application'
        verbose_name_plural = 'Aid decline applications'
		
class ProxyAidDecline(AidDeclineModel):
	class Meta:
		proxy = True
		app_label = 'Financial_Aid'
		verbose_name = 'Aid Decline Form'

