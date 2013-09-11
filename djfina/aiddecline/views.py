#I need all the imports below
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

#Include the form
from djfina.aiddecline.forms import AidDeclineForm

# Create your views here.
def index(request):
	if request.POST: #If we make a POST
		form = AidDeclineForm(request.POST) #Save the contents of the form in a variable
		if form.is_valid(): #If the form is valid
			form.save() #Save the form to the database table
			form = AidDeclineForm() #Clear out the form
			submitted = True #Boolean flag that we finished the form
			return render(request, 'aiddecline/form.html', {
                'form': form,
                'submitted': submitted
            })
            
	else:
		form = AidDeclineForm() #An unbounded form
	return render(request, 'aiddecline/form.html', {
	    'form': form,
	})

