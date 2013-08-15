from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from djfina.teachgrant.forms import TeachGrantForm

# Create your views here.
def submitted(request):
	return render(request, 'other/submitted.html')
	
def create(request):
	if request.POST:
		form = TeachGrantForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('http://google.com')
			
			
	else:
		form = TeachGrantForm()
	return render(request, 'teachgrant/form.html', {'form': form})

