from django import forms
from djfina.teachgrant.models import TeachGrant
from django.db import models
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.core import validators

def must_be_true(value):
	if value == False:
		raise ValidationError(message='this box must be checked', code='not_checked')

class TeachGrantForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(TeachGrantForm, self).__init__(*args, **kwargs)
		self.fields['undergrad_enrolled_in_grant_eligible_program'].label = mark_safe("<b>Undergraduate students only: </b>")
		self.fields['grad_enrolled_in_grant_eligible_program'].label = mark_safe('<b>Graduate Students: </b>')
		self.fields['filed_fafsa'].label = 'I filed or will file a Free Application for Federal Student Aid (FAFSA) for the 2013-2014 academic year.'
		self.fields['understand_conditions'].label = 'I understand that if I am awarded a Federal TEACH Grant, I must do the following:'
		self.fields['gpa_requirements'].choices = self.fields['gpa_requirements'].choices[1:]
		self.fields['filed_fafsa'].validators = [must_be_true]
		self.fields['understand_conditions'].validators = [must_be_true]
	class Meta:
		model = TeachGrant
		widgets = {
			'gpa_requirements': forms.RadioSelect()
		}
