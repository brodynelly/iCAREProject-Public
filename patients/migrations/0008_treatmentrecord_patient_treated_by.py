# Generated by Django 5.1.2 on 2024-10-29 21:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0007_auto_20241027_1843'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TreatmentRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('Unassigned', 'Unassigned'), ('Nurse Assigned', 'Nurse Assigned'), ('Doctor Assigned', 'Doctor Assigned')], default='Unassigned', max_length=20)),
                ('num_of_nurses', models.IntegerField(default=0)),
                ('assigned_doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_doctor', to=settings.AUTH_USER_MODEL)),
                ('assigned_nurses', models.ManyToManyField(related_name='assigned_nurses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='treated_by',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='patients.treatmentrecord'),
        ),
    ]
