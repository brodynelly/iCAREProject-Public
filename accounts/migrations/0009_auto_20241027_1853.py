# Generated by Django 5.1.2 on 2024-10-27 18:53

from django.db import migrations

def update_customuser_fields(apps, schema_editor):
    # Get the CustomUser model using apps.get_model to avoid import issues during migration
    CustomUser = apps.get_model('accounts', 'CustomUser')
    Role = apps.get_model('accounts', 'Role')
    Geocode = apps.get_model('patients', 'Geocode')

    # Iterate over all CustomUser records and fill in missing fields
    for user in CustomUser.objects.all():
        # Update the username if it is missing
        if not user.username:
            user.username = user.email.split('@')[0] if user.email else f"user_{user.pk}"

        # Update the profession if it is missing
        if not user.profession:
            user.profession = "Unspecified"

        # Update the role if it is missing
        if not user.role:
            default_role = Role.objects.first()  # You can set a specific role if you prefer
            user.role = default_role

        # Update the primary_geocode if it is missing
        if not user.primary_geocode:
            default_geocode = Geocode.objects.first()  # You can set a specific geocode if you prefer
            user.primary_geocode = default_geocode

        # Save the user instance after updating fields
        user.save()

class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0008_auto_20241027_1827"),
    ]

    operations = [
        migrations.RunPython(update_customuser_fields),
    ]
