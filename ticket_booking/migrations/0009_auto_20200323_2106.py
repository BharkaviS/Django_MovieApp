# Generated by Django 2.2.5 on 2020-03-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_booking', '0008_auto_20200322_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedetails',
            name='Tickets_current',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='moviedetails',
            name='Tickets_totprice',
            field=models.IntegerField(default=0),
        ),
    ]
