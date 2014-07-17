from django import forms
from djfina.teachgrant.models import TeachGrant
from django.db import models
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.core import validators
import re

def must_be_true(value):
    if value == False:
        raise ValidationError(message='Must be checked', code='not_checked')

class TeachGrantForm(forms.ModelForm):
    
    class Meta:
        model = TeachGrant
        widgets = {
            'gpa_requirements': forms.RadioSelect()
        }
        
    def __init__(self, *args, **kwargs):
        super(TeachGrantForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = self.cleaned_data #Grabs the clean data
        gpa = cleaned_data.get('gpa_requirements') 
        undergrad = cleaned_data.get("undergrad_eligible")
        grad = cleaned_data.get("grad_eligible")
        
        if gpa == 'continuing undergrad and grad students':
            if undergrad == True and grad == True:
                msg = u'Please select only one'
                self._errors['undergrad_eligible'] = self.error_class([msg]) #Creates an error message for this object
                self._errors['grad_eligible'] = self.error_class([msg])
                
                del cleaned_data['undergrad_eligible']
                del cleaned_data['grad_eligible']
                
            elif undergrad == False and grad == False:
                msg = u'Please select an option'
                self._errors['undergrad_eligible'] = self.error_class([msg])
                
                del cleaned_data['undergrad_eligible']
                del cleaned_data['grad_eligible']
            
        return cleaned_data
    
    def clean_student_name(self):
        data = self.cleaned_data['student_name']
        if not re.match(r'^((?:[a-zA-Z]+\s?){1,2}[a-zA-Z]+)$', data):
            raise forms.ValidationError('Invalid characters')
        return data
    
    def clean_carthage_id(self):
        data = self.cleaned_data['carthage_id']
        if not re.match(r'^(\d{5,7})$', data):
            raise forms.ValidationError('Invalid ID')
        return data
    
    def clean_filed_fafsa(self):
        data = self.cleaned_data['filed_fafsa']
        if not data:
            raise forms.ValidationError('Must be checked')
        return data
    
    def clean_understand_conditions(self):
        data = self.cleaned_data['understand_conditions']
        if not data:
            raise forms.ValidationError('Must be checked')
        return data
