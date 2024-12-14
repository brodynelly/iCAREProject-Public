# Generated by Django 5.1.2 on 2024-10-23 19:41

from django.db import migrations
import datetime
def create_or_update_patients(apps, schema_editor):
    Patient = apps.get_model('patients', 'Patient')
    Geocode = apps.get_model('patients', 'Geocode')
    
    # Delete all existing patients
    Patient.objects.all().delete()
    
    # Create geocodes
    geocode1, _ = Geocode.objects.get_or_create(name="North Area", description="Northern Region")
    geocode2, _ = Geocode.objects.get_or_create(name="South Area", description="Southern Region")
    
    # Create new patients
    patients = [
        Patient(name="John Doe", address="123 Elm Street", date_of_birth=datetime.date(1980, 5, 15), height=70, weight=180, blood_group="O+", bed_id="B101", treatment_area="Cardiology", geocode=geocode1),
        Patient(name="Jane Smith", address="456 Oak Avenue", date_of_birth=datetime.date(1990, 7, 20), height=65, weight=150, blood_group="A-", bed_id="B102", treatment_area="Neurology", geocode=geocode2),
        Patient(name="Charlie Brown", address="789 Pine Lane", date_of_birth=datetime.date(1975, 3, 10), height=68, weight=160, blood_group="B+", bed_id="B103", treatment_area="Orthopedics", geocode=geocode1),
        Patient(name="Alice Wonderland", address="101 Maple Drive", date_of_birth=datetime.date(1985, 11, 5), height=62, weight=130, blood_group="AB-", bed_id="B104", treatment_area="Pediatrics", geocode=geocode2),
        Patient(name="Bruce Wayne", address="Wayne Manor", date_of_birth=datetime.date(1972, 2, 19), height=74, weight=210, blood_group="A+", bed_id="B105", treatment_area="Oncology", geocode=geocode1),
        Patient(name="Clark Kent", address="Kent Farm", date_of_birth=datetime.date(1983, 6, 18), height=76, weight=220, blood_group="B-", bed_id="B106", treatment_area="General Medicine", geocode=geocode2),
        Patient(name="Diana Prince", address="Themyscira", date_of_birth=datetime.date(1988, 4, 23), height=70, weight=170, blood_group="AB+", bed_id="B107", treatment_area="Gynecology", geocode=geocode1),
        Patient(name="Peter Parker", address="20 Ingram Street", date_of_birth=datetime.date(1995, 8, 10), height=67, weight=155, blood_group="O-", bed_id="B108", treatment_area="Dermatology", geocode=geocode2),
    ]
    Patient.objects.bulk_create(patients)

class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_geocode_patient_geocode'),
    ]

    operations = [
       migrations.RunPython(create_or_update_patients),
    ]