from django import forms
from django.db import models

# Create your models here.
class ScholarshipModel(models.Model):

	class Meta:
		verbose_name = 'Entries'
		verbose_name_plural = 'Entry'
	
	scholarship_name = models.CharField(blank=False,max_length=100)
	name_of_donor_or_organization = models.CharField(blank=False,max_length=100)
	yearly_award = models.IntegerField(blank=False,max_length=7)
	years_award_is_available = models.IntegerField(blank=False,max_length=2)
	
	FUNDS_WILL_BE_SENT_TO = (
		('school', 'School'),
		('student', 'Student'),
	)
	
	funds_will_be_sent_to = models.CharField(max_length=10,choices=FUNDS_WILL_BE_SENT_TO)
	
#class ScholarshipProxy(ScholarshipModel):
#	class Meta:
#		proxy = True
#		app_label = 'Registrar'
#		verbose_name = 'b'
		
	
