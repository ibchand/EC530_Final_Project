# Generated by Django 4.0.4 on 2022-05-08 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TreeAPI', '0005_journey_origin_lat_journey_origin_long'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journey',
            name='success',
        ),
        migrations.AlterField(
            model_name='journey',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]