# Generated by Django 3.2.5 on 2021-08-18 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_auto_20210811_0441'),
    ]

    operations = [
        migrations.AddField(
            model_name='takeappointment',
            name='Time_pet',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
