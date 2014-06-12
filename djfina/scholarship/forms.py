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
    
    def clean_scholarship_name(self):
        data = self.cleaned_data['scholarship_name']
        if not re.match(r'^((?:[\w]+\s?)+[\w]+)$', data):
            raise forms.ValidationError('Only use letters, spaces, hypens and numbers')
        return data
        
    def clean_name_of_donor_or_organization(self):
        data = self.cleaned_data['name_of_donor_or_organization']
        if not re.match(r'^((?:[\w]+\s?)+[\w]+)$', data):
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
