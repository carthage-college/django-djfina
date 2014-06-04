from django.conf.urls import patterns, include, url

urlpatterns = patterns('djfina.teachgrant.views',
    url(r'^$', 'create', name='create'),
)
