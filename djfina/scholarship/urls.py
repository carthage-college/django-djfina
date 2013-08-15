from django.conf.urls import patterns, include, url

urlpatterns = patterns('djfina.scholarship.views',
	url(r'^$', 'index', name='index'),
)
