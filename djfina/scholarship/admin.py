from django.contrib import admin
from djfina.scholarship.models import ScholarshipModel#, ScholarshipProxy


class ScholarshipAdmin(admin.ModelAdmin):
	search_fields = ['scholarship_name']
	list_display = ('scholarship_name','name_of_donor_or_organization')
	list_filter = ('scholarship_name','name_of_donor_or_organization')

admin.site.register(ScholarshipModel, ScholarshipAdmin)
