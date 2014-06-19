#Need these below
from django import forms
from django.db import models
from django.core import validators
from djfina.aiddecline.models import AidDeclineModel, OtherModel
import re

class AidDeclineForm(forms.ModelForm):
    
    CHOICES = (
        ("FDLS", 'Federal Direct Loan - Subsidized'),
        ("FDLU", 'Federal Direct Loan - Unsubsidized'),
        ("FPL", 'Federal Perkins Loan'),
        ("WORK", 'Federal Work-Study'),
    )    
    
    aid = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CHOICES)
    
    class Meta:
        model = AidDeclineModel #Fields come from the 'AidDeclineModel' model
    
    def __init__(self, *args, **kwargs):
        super(AidDeclineForm, self).__init__(*args, **kwargs)
        
    def clean_student_id(self):
        data = self.cleaned_data['student_id']
        if not re.match(r'^(\d{5,7})$', data):
            raise forms.ValidationError("Invalid ID")
        return data
    
    def clean_name(self):
        data = self.cleaned_data['name']
        if not re.match(r'^((?:[a-zA-Z]+\s?){1,2}[a-zA-Z]+)$', data):
            raise forms.ValidationError('Invalid characters')
        return data

class OtherForm(forms.Form):
    other = forms.CharField()