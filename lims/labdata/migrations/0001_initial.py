# Generated by Django 4.2.11 on 2024-03-23 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0005_remove_sample_specimen_remove_sample_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cat_num', models.CharField(max_length=200)),
                ('lot_num', models.CharField(max_length=200)),
                ('exp', models.DateField()),
                ('in_use', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sci_name', models.CharField(max_length=200, unique=True)),
                ('common_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collect_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SampleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('reportable_results', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Specimen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('cohort', models.CharField(max_length=100)),
                ('organism', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labdata.organism')),
            ],
        ),
        migrations.CreateModel(
            name='SampleResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('results', models.TextField()),
                ('analyst', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.analyst')),
                ('reagent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='labdata.inventory')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labdata.sample')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labdata.test')),
            ],
        ),
        migrations.AddField(
            model_name='sample',
            name='specimen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labdata.specimen'),
        ),
        migrations.AddField(
            model_name='sample',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='labdata.sampletype'),
        ),
    ]
