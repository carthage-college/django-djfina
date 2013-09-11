#Need these below
from django import forms
from django.db import models
from django.core import validators
from djfina.aiddecline.models import AidDeclineModel

class AidDeclineForm(forms.ModelForm):
    
    class Meta:
	    model = AidDeclineModel #Fields come from the 'AidDeclineModel' model
	
    def __init__(self, *args, **kwargs):
        super(AidDeclineForm, self).__init__(*args, **kwargs)
        
        #Custom labels for the fields
        self.fields['direct_sub'].label = 'Federal Direct Loan - Subsidized'
        self.fields['direct_unsub'].label = 'Federal Direct Loan - Unsubsidized'
        self.fields['perkins'].label = 'Federal Perkins Loan'
        self.fields['work_study'].label = 'Federal Work-Study'
        self.fields['student_id'].label = 'ID'
        self.fields['other1'].label = 'Other'
        self.fields['other2'].label = 'Other'
        
        #Custom validators for the fields
        self.fields['name'].validators = [validators.RegexValidator(regex=('^[a-zA-Z\']+[a-zA-Z\s\.\-\']+$'),message='Invalid characters',code='bad_name')]
        self.fields['student_id'].validators = [validators.RegexValidator(regex=('^\d{5,7}$'),message='Invalid id',code='bad_id')]
        
        #Custom error messages for the fields
        self.fields['name'].error_messages = {'required':'Required','Invalid':'Invalid characters'}
        self.fields['student_id'].error_messages = {'required':'Required','Invalid':'Invalid id'}
