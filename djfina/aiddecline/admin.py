from django.contrib import admin
from djfina.aiddecline.models import AidDecline, ProxyAidDecline

class FormAdmin(admin.ModelAdmin):
	readonly_fields = ('submit_date',)
	
admin.site.register(ProxyAidDecline, FormAdmin)
