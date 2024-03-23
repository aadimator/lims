# Generated by Django 4.2.11 on 2024-03-23 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0003_remove_role_role_name_remove_role_role_permissions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='group',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='role', to='auth.group'),
        ),
    ]
