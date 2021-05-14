
from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=('given_name','family_name','date_of_birth','gender','street','house_number','city','pc','state','country','tel','email','hp','insur_number','delivery_date' )