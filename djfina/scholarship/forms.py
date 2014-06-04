from django import forms
from datetime import date #Used for dynamic years
from django.core import validators
from django.forms.formsets import BaseFormSet #Need this for the formset
from django.core.exceptions import ValidationError
import re

from djfina.scholarship.models import ScholarshipModel


class ScholarshipForm(forms.ModelForm):

    class Meta:
        model = ScholarshipModel

    def __init__(self, *args, **kwargs):
        super(ScholarshipForm, self).__init__(*args, **kwargs)
        
        #self.fields['years_award_is_available'].label = 'Award is available until'
        #self.fields['name_of_donor_or_organization'].label = 'Donor / Organization'
        #self.fields['files'].label = 'File'
        
        #Custom validation for the fields
        #self.fields['scholarship_name'].validators = [validators.RegexValidator(regex=(r'^[a-zA-Z]+[a-zA-Z\s0-9-]*$'),message='Only use letters, spaces, hypens and numbers',code='a')]
        #self.fields['name_of_donor_or_organization'].validators = [validators.RegexValidator(regex=(r'^[a-zA-Z]+[a-zA-Z\s-]*$'),message='Only use letters, spaces and hypens',code='a')]
        #self.fields['yearly_award'].validators = [validators.RegexValidator(regex=(r'^\d{1,7}$'),message='Use only digits (no negatives, < 1,000,000)',code='a')]
        
        #Custom error messages for the fields
        #self.fields['scholarship_name'].error_messages = {'required':'Required','invalid':'Invalid characters'}
        #self.fields['name_of_donor_or_organization'].error_messages = {'required':'Required','invalid':'Invalid characters'}
       # self.fields['yearly_award'].error_messages = {'required':'Required','invalid':'Must be between 1 and 7 digits long'}
       
    def clean_scholarship_name(self):
        data = self.cleaned_data['scholarship_name']
        if not re.match(r'^[a-zA-Z]+[a-zA-Z\s0-9-]*$', data):
            raise forms.ValidationError('Only use letters, spaces, hypens and numbers')
        return data
        
    def clean_name_of_donor_or_organization(self):
        data = self.cleaned_data['name_of_donor_or_organization']
        if not re.match(r'^[a-zA-Z]+[a-zA-Z\s-]*$', data):
            raise forms.ValidationError('Only use letters, spaces and hypens')
        return data
        
    def clean_yearly_award(self):
        data = self.cleaned_data['yearly_award']
        if not re.match(r'^\d{1,7}$', data):
            raise forms.ValidationError('Use only digits (no negatives, < 1,000,000)')
        return data


class RequiredFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        
        self.forms[0].empty_permitted = False
