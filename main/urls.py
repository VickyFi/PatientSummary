from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('patients/', views.patients, name='patients'),
    path('add-patient',views.addPatient, name='add-patient'),
    path('edit-patient/<int:id>', views.editPatient, name='edit-patient'),
    path('delete-patient/<int:id>',views.deletePatient,name='delete-patient'),
]