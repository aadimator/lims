# Generated by Django 4.2.11 on 2024-03-27 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labdata', '0003_alter_specimen_sample_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specimen',
            old_name='sample_name',
            new_name='specimen_id',
        ),
    ]
