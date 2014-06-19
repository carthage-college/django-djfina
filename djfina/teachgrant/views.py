#I need all the imports below
from django import forms
from django.shortcuts import render
from djzbar.settings import INFORMIX_EARL_TEST
from sqlalchemy import create_engine
from django.http import HttpResponse, HttpResponseRedirect
from djfina.teachgrant.forms import TeachGrantForm
from djfina.teachgrant.models import TeachGrant
from django.core.context_processors import csrf
from django.template import RequestContext  # For CSRF
import datetime

# Create your views here.
def submitted(request):
    return render(request, 'other/submitted.html')
    
def create(request):
    if request.POST:
        (a, created) = TeachGrant.objects.get_or_create(carthage_id=request.POST['carthage_id']) 
        form = TeachGrantForm(request.POST, instance=a)
        form.fields['student_name'].widget = forms.HiddenInput()
        form.fields['carthage_id'].widget = forms.HiddenInput()
        if form.is_valid():
            form.save()
            submitted = True
            
            return render(request, 'teachgrant/form.html', {
                'form': form,
                'year': datetime.datetime.now().year,
                'year2': datetime.datetime.now().year + 1,
                'submitted': submitted
            })
            
            
    else:
        form = TeachGrantForm()
        if request.GET:
            engine = create_engine(INFORMIX_EARL_TEST)
            connection = engine.connect()
            sql = 'SELECT id_rec.id, id_rec.fullname FROM id_rec WHERE id_rec.id = %d' % (int(request.GET['carthage_id']))
            student = connection.execute(sql)
            for thing in student:
                form.fields['carthage_id'].initial = thing['id']
                form.fields['student_name'].initial = thing['fullname']
            connection.close()
        form.fields['carthage_id'].widget = forms.HiddenInput()
        form.fields['student_name'].widget = forms.HiddenInput()            
        
        # For CSRF protection
        # See http://docs.djangoproject.com/en/dev/ref/contrib/csrf/ 
        c = {'form': form,
            }
        c.update(csrf(request))
    return render(request, 'teachgrant/form.html', {
        'form': form,
        'year': datetime.datetime.now().year, 
        'year2': datetime.datetime.now().year + 1
    })

