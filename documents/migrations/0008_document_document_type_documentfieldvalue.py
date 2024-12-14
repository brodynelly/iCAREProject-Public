# Generated by Django 5.1.2 on 2024-10-25 16:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0007_documenttype_documentfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='document_type',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='documents.documenttype'),
        ),
        migrations.CreateModel(
            name='DocumentFieldValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_values', to='documents.document')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.documentfield')),
            ],
        ),
    ]