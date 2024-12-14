# Generated by Django 5.1.2 on 2024-10-23 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('blood_group', models.CharField(max_length=3)),
                ('bed_id', models.CharField(max_length=255)),
                ('treatment_area', models.CharField(max_length=255)),
            ],
        ),
    ]