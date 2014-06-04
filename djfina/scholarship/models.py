from django import forms
from django.db import models
import datetime

#For dynamically creating years
year = datetime.date.today().year #Get today's year
YEARS = (('unkn', 'Unknown'),) + tuple((i, i) for i in range(year, year + 11)) #Save the variable

# Create your models here.
class ScholarshipModel(models.Model):

    scholarship_name = models.CharField(max_length=100)
    name_of_donor_or_organization = models.CharField(max_length=100, verbose_name='Donor / Organization')
    yearly_award = models.IntegerField(max_length=7)

    years_award_is_available = models.CharField(max_length=11, choices=YEARS, verbose_name='Award is available until') #Choices dynamically created for this field in forms.py

    FUNDS_WILL_BE_SENT_TO = (
        ('school', 'School'),
        ('student', 'Student'),
    )

    funds_will_be_sent_to = models.CharField(max_length=10,choices=FUNDS_WILL_BE_SENT_TO)
    files = models.FileField(upload_to='files', verbose_name='File')

#class ScholarshipProxy(ScholarshipModel):
#    class Meta:
#        proxy = True
#        app_label = 'Registrar'
#        verbose_name = 'b'
