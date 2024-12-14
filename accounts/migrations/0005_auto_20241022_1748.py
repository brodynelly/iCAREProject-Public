# Generated by Django 5.1.2 on 2024-10-22 17:48

from django.db import migrations

def create_roles(apps, schema_editor):
    Role = apps.get_model("accounts", "Role")
    Role.objects.get_or_create(name="doctor")
    Role.objects.get_or_create(name="nurse")
    Role.objects.get_or_create(name="admin")

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_email'),
    ]

    operations = [
        migrations.RunPython(create_roles),
    ]
