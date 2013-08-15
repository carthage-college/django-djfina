# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import generic
from django.forms.formsets import formset_factory

from djfina.scholarship.models import ScholarshipModel
from djfina.scholarship.forms import ScholarshipForm

def index(request):

	ScholarshipFormSet = formset_factory(ScholarshipForm, extra=7)
	#formset = ScholarshipFormSet()
	
	if request.method == 'POST':
		formset = ScholarshipFormSet(request.POST)
		if formset.is_valid():
			for a in formset:
				a.clean()
					#a.save()
			#formset.save()
			
			return HttpResponseRedirect('http://google.com')
			
	else:
		formset = ScholarshipFormSet()
		
	return render(request, 'scholarship/form.html', {
		'formset': formset,
	})
	
#def submitted(request):
#	return render(request, 'scholarship_app/submitted.html')
