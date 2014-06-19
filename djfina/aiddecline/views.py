#I need all the imports below
from django import forms
from djzbar.settings import INFORMIX_EARL_TEST
from sqlalchemy import create_engine
from djfina.aiddecline.forms import AidDeclineForm, OtherForm
from djfina.aiddecline.models import AidDeclineModel, OtherModel
from django.shortcuts import render
from django.forms.formsets import formset_factory, BaseFormSet #For formsets
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext  # For CSRF

#Include the form
from djfina.aiddecline.forms import AidDeclineForm

# Create your views here.
def index(request):
    OtherFormset = formset_factory(OtherForm)
    if request.POST:
        (a, created) = AidDeclineModel.objects.get_or_create(student_id=request.POST['student_id']) 
        form = AidDeclineForm(request.POST, instance=a) #Save the contents of the form in a variable        
        form.fields['name'].widget = forms.HiddenInput()
        form.fields['student_id'].widget = forms.HiddenInput()
        other_formset = OtherFormset(request.POST, prefix='other')    
        if form.is_valid() and other_formset.is_valid(): #If the form is valid
            form_instance = form.save() #Save the form to the database table
            for f in other_formset:
                other = f.save(commit=False)
                other.list = form_instance
                other.save()
            form = AidDeclineForm() #Clear out the form
            other_formset = OtherFormset(prefix='other')
            submitted = True #Boolean flag that we finished the form
            return render(request, 'aiddecline/design.html', {
                'form': form,
                'submitted': submitted
            })            
    else:
        form = AidDeclineForm() #An unbounded form
        if request.GET:
            engine = create_engine(INFORMIX_EARL_TEST)
            connection = engine.connect()
            sql = 'SELECT id_rec.id, id_rec.fullname FROM id_rec WHERE id_rec.id = %d' % (int(request.GET['student_id']))
            student = connection.execute(sql)
            for thing in student:
                form.fields['student_id'].initial = thing['id']
                form.fields['name'].initial = thing['fullname']
            connection.close()
        form.fields['student_id'].widget = forms.HiddenInput()
        form.fields['name'].widget = forms.HiddenInput()
        
        other_formset = OtherFormset(prefix='other')
        
        # For CSRF protection
        # See http://docs.djangoproject.com/en/dev/ref/contrib/csrf/ 
        c = {'form': form,
             'other_formset': other_formset,
            }
        c.update(csrf(request))
    
    return render(request, 'aiddecline/design.html', {
        'form': form,
        'other_formset': other_formset,
    })

