from django.contrib import admin
from djfina.teachgrant.models import TeachGrant, ProxyTeachGrant

class FormAdmin(admin.ModelAdmin):
    readonly_fields = ('submit_date',)
    
admin.site.register(ProxyTeachGrant, FormAdmin)
