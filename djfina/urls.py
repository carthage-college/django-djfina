from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^aiddecline/', include('djfina.aiddecline.urls')),
    url(r'^scholarship/', include('djfina.scholarship.urls')),
    url(r'^teachgrant/', include('djfina.teachgrant.urls')),
)
