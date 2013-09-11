from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from djfina.teachgrant.forms import TeachGrantForm
import datetime

# Create your views here.
def submitted(request):
	return render(request, 'other/submitted.html')
	
def create(request):
	if request.POST:
		form = TeachGrantForm(request.POST)
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
	return render(request, 'teachgrant/form.html', {
	    'form': form,
	    'year': datetime.datetime.now().year, 
	    'year2': datetime.datetime.now().year + 1
	})

