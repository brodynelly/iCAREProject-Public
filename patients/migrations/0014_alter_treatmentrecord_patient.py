# Generated by Django 5.1.2 on 2024-10-30 01:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0013_treatmentrecord_patient_alter_patient_treated_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatmentrecord',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='treatment', to='patients.patient'),
        ),
    ]