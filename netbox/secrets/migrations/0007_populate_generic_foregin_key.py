# Generated by Django 2.0.8 on 2018-08-10 15:29
 from django.db import migrations
 def migrate_device_secret(apps, schema_editor):
    """
        Move data from device foreign key into GenericForeignKey
    """
    Secret = apps.get_model('secrets', 'Secret')
    if Secret.objects.count() > 0:
        ContentType = apps.get_model('contenttypes', 'ContentType')
         secret_device_content_type = ContentType.objects.get(app_label='dcim', model='device')
         for secret in Secret.objects.all():
            secret.content_type = secret_device_content_type
            secret.object_id = secret.device.pk
            secret.save()
 class Migration(migrations.Migration):
     dependencies = [
        ('dcim', '0058_relax_rack_naming_constraints'),
        ('secrets', '0006_foreign_key_generic'),
    ]
     operations = [
        migrations.RunPython(migrate_device_secret)
    ]
