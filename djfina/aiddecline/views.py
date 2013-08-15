from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from djfina.aiddecline.forms import AidDeclineForm, OtherForm
from django.forms.formsets import formset_factory

# Create your views here.
def submitted(request):
	return render(request, 'other/submitted.html')
	
	
def create(request):
	OtherFormSet = formset_factory(OtherForm, extra=2)
	if request.POST:
		other_formset = OtherFormSet(request.POST)
		form = AidDeclineForm(request.POST)
		if form.is_valid() and other_formset.is_valid():
			form_instance = form.save()
			other = []
			for f in other_formset:
				if f.clean():
					other.append(f.cleaned_data['name'])
			if len(other) >=1:
				form_instance.other1 = other[0]
			if len(other) >=2:
				form_instance.other2 = other[1]
			form_instance.save()
			return HttpResponseRedirect('http://google.com')
		
		
	else:
		other_formset = OtherFormSet()
		form = AidDeclineForm()
	return render(request, 'aiddecline/form.html', {'form': form, 'other_formset': other_formset})

