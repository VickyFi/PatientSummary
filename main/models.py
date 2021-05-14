# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdministrativeData(models.Model):
    country = models.CharField(max_length=100)
    created_date = models.DateField()
    updated_date = models.DateField()
    nature = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administrative_data'


class Agent(models.Model):
    agent_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'agent'


class Allergy(models.Model):
    allergy_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    agent = models.ForeignKey(Agent, models.DO_NOTHING, blank=True, null=True)
    onset_date = models.DateField(blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allergy'


class BloodGroup(models.Model):
    result = models.CharField(max_length=255, blank=True, null=True)
    performed_date = models.DateField(blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blood_group'


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    contact_role = models.CharField(max_length=100, blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact'


class Disease(models.Model):
    disease_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'disease'


class HpContact(models.Model):
    hp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'hp_contact'


class Invalidity(models.Model):
    invalidity_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invalidity'


class MedAlert(models.Model):
    alert_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'med_alert'


class MedDevice(models.Model):
    device_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    implant_date = models.DateField()
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'med_device'


class MedProblem(models.Model):
    problem_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    onset_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    resolution = models.CharField(max_length=255, blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'med_problem'


class Medication(models.Model):
    medication_id = models.AutoField(primary_key=True)
    medicine = models.ForeignKey('Medicine', models.DO_NOTHING, blank=True, null=True)
    units = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    onset_date = models.DateField()
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medication'


class Medicine(models.Model):
    medicine_id = models.AutoField(primary_key=True)
    active_ingredient_brand_name = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)
    form = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'medicine'


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    given_name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    street = models.CharField(max_length=100, blank=True, null=True)
    house_number = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    pc = models.CharField(max_length=10, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    tel = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    hp = models.ForeignKey(HpContact, models.DO_NOTHING)
    insur_number = models.CharField(max_length=100)
    delivery_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.family_name
    

    class Meta:
        managed = False
        db_table = 'patient'


class Recommendation(models.Model):
    recom_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recommendation'


class SocialHistory(models.Model):
    date_range = models.CharField(max_length=100, blank=True, null=True)
    observations = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'social_history'


class Surgery(models.Model):
    surgery_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    procedure_date = models.DateField()
    patient = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surgery'


class Vaccination(models.Model):
    vaccination_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=100)
    vaccination_date = models.DateField()
    patient = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vaccination'


class VaccinationDisease(models.Model):
    vaccination = models.OneToOneField(Vaccination, models.DO_NOTHING, primary_key=True)
    disease = models.ForeignKey(Disease, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vaccination_disease'
        unique_together = (('vaccination', 'disease'),)


class VitalSigns(models.Model):
    systolic = models.IntegerField(blank=True, null=True)
    diastolic = models.IntegerField(blank=True, null=True)
    measured_date = models.DateField(blank=True, null=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vital_signs'
