# Generated by Django 2.2.5 on 2020-03-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_booking', '0005_auto_20200321_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedetails',
            name='trailer',
            field=models.TextField(default='null'),
        ),
    ]
