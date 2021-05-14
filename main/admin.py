from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display=('given_name','family_name', 'insur_number', 'hp')
admin.site.register(Patient,PatientAdmin)