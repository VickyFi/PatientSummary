from django.shortcuts import render,HttpResponse,redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Patient
from django.db.models import Q
from .forms import PatientForm
from django.core.paginator import Paginator

def home(request):
    return render(request, 'home.html')

def patients(request):
    return render(request,'patients.html',{'patients': Patient.objects.all()})

# Add Patient
def addPatient(request):
    form=PatientForm
    if request.method=='POST':
        saveForm=PatientForm(request.POST)
        if saveForm.is_valid():
            saveForm.save()
            messages.success(request,'Data has been added.')
    return render(request,'add-patient.html',{'form':form})

# Update Patient
def editPatient(request,id):
    patient=Patient.objects.get(patient_id=id)
    if request.method=='POST':
        saveForm=PatientForm(request.POST,instance=patient)
        if saveForm.is_valid():
            saveForm.save()
            messages.success(request,'Data has been updated.')
    form=PatientForm(instance=patient)
    return render(request,'edit-patient.html',{'form':form})

# Delete
def deletePatient(request,id):
    Patient.objects.filter(patient_id=id).delete()
    return redirect('/')