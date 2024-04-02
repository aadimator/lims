# Generated by Django 4.2.11 on 2024-04-02 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_analyst_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyst',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='analyst',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='analyst',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
