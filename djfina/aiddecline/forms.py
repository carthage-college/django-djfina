from django import forms
from djfina.aiddecline.models import AidDecline
from django.db import models
from django.core import validators

class AidDeclineForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(AidDeclineForm, self).__init__(*args, **kwargs)
		self.fields['direct_sub'].label = 'Federal Direct Loan - Subsidized'
		self.fields['direct_unsub'].label = 'Federal Direct Loan - Unsubsidized'
		self.fields['perkins'].label = 'Federal Perkins Loan'
		self.fields['work_study'].label = 'Federal Work-Study'
		self.fields['student_id'].label = 'ID:'
		self.fields['name'].validators = [validators.RegexValidator(regex=('^[a-zA-Z]+[a-zA-Z\s\.-]*$'),message='Please enter a valid name',code='a')]
		self.fields['student_id'].validators = [validators.RegexValidator(regex=('^\d{7}$'),message='Use a 7 digit number',code='b')]
		
	class Meta:
		model = AidDecline
		exclude = ['other1', 'other2']
		
class OtherForm(forms.Form):
	name = forms.CharField(max_length=30, label='Other')
	
