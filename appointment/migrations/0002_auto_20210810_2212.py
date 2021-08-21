# Generated by Django 3.2.5 on 2021-08-11 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='takeappointment',
            name='pet_name',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='clinic_name',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='department',
            field=models.CharField(choices=[('Fitness Specialist', 'Fitness Specialist'), ('Hygiene Specialist', 'Hygiene Specialist'), ('Pychiatric Specialist', 'Psychiatric Specialist'), ('Mobility Specialist', 'Mobility Specialist'), ('Surgery Specialist', 'Surgery Specialist')], max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='end_time',
            field=models.CharField(default=' ', max_length=10),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='full_name',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='institute_name',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='location',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='qualification_name',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='start_time',
            field=models.CharField(default=' ', max_length=10),
        ),
        migrations.AlterField(
            model_name='takeappointment',
            name='full_name',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='takeappointment',
            name='phone_number',
            field=models.CharField(default=' ', max_length=120),
        ),
    ]
