# Create your views here.
import datetime
from django.views import generic
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.forms.formsets import formset_factory
from django.http import HttpResponse, HttpResponseRedirect


from djfina.scholarship.models import ScholarshipModel
from djfina.scholarship.forms import ScholarshipForm, RequiredFormSet

cur_year = datetime.datetime.now().year
cur_year2 = (datetime.datetime.now().year+1)

def index(request):

    ScholarshipFormSet = formset_factory(ScholarshipForm, extra=1, formset=RequiredFormSet)
    if request.method == 'POST':
        formset = ScholarshipFormSet(request.POST, files=request.FILES, prefix='Sc')
        if 'add' in request.POST:
            array=[({
                    'scholarship_name':formset.data['Sc-%s-scholarship_name' % (i)],
                    'name_of_donor_or_organization':formset.data['Sc-%s-name_of_donor_or_organization' % (i)],
                    'yearly_award':formset.data['Sc-%s-yearly_award' % (i)],
                    'years_award_is_available':formset.data['Sc-%s-years_award_is_available' % (i)],
                    'funds_will_be_sent_to':formset.data['Sc-%s-funds_will_be_sent_to' % (i)],
                    'files':formset.data['Sc-%r-files' % (i)]
                }) for i in range(0,int(formset.data['Sc-TOTAL_FORMS']))]
            formset = ScholarshipFormSet(prefix='Sc', initial=array)
        else:
            submitted = False
            if formset.is_valid():
                for f in formset:
                    if f.clean():
                        f.save()
                        
                formset = ScholarshipFormSet(prefix='Sc')
                submitted = True
            return render(request, 'scholarship/form.html', {
                'form': formset,
                'submitted': submitted
            })
            
    else:
        formset = ScholarshipFormSet(prefix='Sc')
        
    return render(request, 'scholarship/form.html', {
        'year': cur_year,
        'year2': cur_year2,
        'form': formset
    })
