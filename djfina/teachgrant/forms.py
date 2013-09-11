from django import forms
from djfina.teachgrant.models import TeachGrant
from django.db import models
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.core import validators

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
        
        #Custom labels for form fields
        self.fields['gpa_requirements'].label = 'Current status'
        self.fields['undergrad_enrolled_in_grant_eligible_program'].label = mark_safe("Undergraduate enrolled in a grant-eligible program")
        self.fields['grad_enrolled_in_grant_eligible_program'].label = mark_safe('Graduate enrolled in a grant-eligible program')
        self.fields['filed_fafsa'].label = 'I agree with the FAFSA conditions'
        self.fields['understand_conditions'].label = 'I understand that if I am awarded a Federal TEACH Grant, I must do the following'
        self.fields['file'].label = 'File'
        
        #Custom regex validation for form fields
        self.fields['student_name'].validators = [validators.RegexValidator(regex='^[a-zA-Z\']+[a-zA-Z\-\s\']+$',message='Invalid characters',code='bad_name')]
        self.fields['carthage_id'].validators = [validators.RegexValidator(regex='^\d{5,7}$',message='Invalid ID',code='bad_id')]
        self.fields['TEACH_grant_eligible_program_of_study'].validators = [validators.RegexValidator(regex='^.+$', message='Required', code='bad_TEACH')]
        self.fields['filed_fafsa'].validators = [must_be_true] #Validation from function on top of file
        self.fields['understand_conditions'].validators = [must_be_true]
        
        #Custom error messages for form fields
        self.fields['carthage_id'].error_messages = {'required':'Required','invalid':'Between 5 and 7 digits'}
        self.fields['student_name'].error_messages = {'required':'Required','invalid':'Invalid characters'}
        self.fields['TEACH_grant_eligible_program_of_study'].error_messages = {'required':'Required','invalid':'Invalid characters'}

    def clean(self):
        cleaned_data = self.cleaned_data #Grabs the clean data
        gpa = cleaned_data.get('gpa_requirements') 
        undergrad = cleaned_data.get("undergrad_enrolled_in_grant_eligible_program")
        grad = cleaned_data.get("grad_enrolled_in_grant_eligible_program")
        
        if gpa == 'continuing undergrad and grad students':
            if undergrad == True and grad == True:
                msg = u'Please select only one'
                self._errors['undergrad_enrolled_in_grant_eligible_program'] = self.error_class([msg]) #Creates an error message for this object
                self._errors['grad_enrolled_in_grant_eligible_program'] = self.error_class([msg])
                
                del cleaned_data['undergrad_enrolled_in_grant_eligible_program']
                del cleaned_data['grad_enrolled_in_grant_eligible_program']
                
            elif undergrad == False and grad == False:
                msg = u'Please select an option'
                self._errors['undergrad_enrolled_in_grant_eligible_program'] = self.error_class([msg])
                
                del cleaned_data['undergrad_enrolled_in_grant_eligible_program']
            
        return cleaned_data
