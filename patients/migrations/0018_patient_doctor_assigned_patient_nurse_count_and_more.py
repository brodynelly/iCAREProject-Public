# Generated by Django 5.1.2 on 2024-10-30 14:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0017_remove_patient_treated_by_delete_treatmentrecord'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='doctor_assigned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='nurse_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patient',
            name='state',
            field=models.CharField(choices=[('unassigned', 'Unassigned'), ('nurse_assigned', 'Nurse Assigned'), ('doctor_assigned', 'Doctor Assigned')], default='unassigned', max_length=15),
        ),
        migrations.CreateModel(
            name='TreatmentRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
                ('worker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('patient', 'worker')},
            },
        ),
        migrations.AddField(
            model_name='patient',
            name='treated_by',
            field=models.ManyToManyField(related_name='patients', through='patients.TreatmentRecord', to=settings.AUTH_USER_MODEL),
        ),
    ]