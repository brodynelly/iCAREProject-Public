# Generated by Django 5.1.2 on 2024-10-30 02:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0014_alter_treatmentrecord_patient'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatmentrecord',
            name='assigned_nurses',
        ),
        migrations.RemoveField(
            model_name='treatmentrecord',
            name='num_of_nurses',
        ),
        migrations.CreateModel(
            name='NurseAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_at', models.DateTimeField(auto_now_add=True)),
                ('nurse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('treatment_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nurse_assignments', to='patients.treatmentrecord')),
            ],
        ),
    ]
