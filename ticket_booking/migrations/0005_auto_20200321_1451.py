# Generated by Django 2.2.5 on 2020-03-21 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_booking', '0004_moviedetails_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedetails',
            name='price',
            field=models.IntegerField(),
        ),
    ]
