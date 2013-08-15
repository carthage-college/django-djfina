from django import forms
from djfina.scholarship.models import ScholarshipModel
from django.core.exceptions import ValidationError
from django.core import validators

class ScholarshipForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ScholarshipForm, self).__init__(*args,**kwargs)
		
		self.fields['scholarship_name'].validators = [validators.RegexValidator(regex=(r'^[a-zA-Z]+[a-zA-Z\s0-9-]*$'),message='Only use letters, spaces, hypens and numbers',code='a')]
		self.fields['name_of_donor_or_organization'].validators = [validators.RegexValidator(regex=(r'^[a-zA-Z]+[a-zA-Z\s-]*$'),message='Only use letters, spaces and hypens',code='a')]
		self.fields['yearly_award'].validators = [validators.RegexValidator(regex=(r'^\d{0,7}$'),message='Use only digits (no negatives, < 1,000,000)',code='a')]
		self.fields['years_award_is_available'].validators = [validators.RegexValidator(regex=(r'^\d{0,2}$'),message='Use only digits (no negatives, < 99)',code='a')]
		self.fields['name_of_donor_or_organization'].label = 'Donor / Organization'

	class Meta:
		model = ScholarshipModel	
