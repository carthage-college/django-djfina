from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

urlpatterns = patterns('djfina.aiddecline.views',
	url(r'^$', 'create', name='create'),
)
