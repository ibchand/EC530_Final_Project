# Generated by Django 4.0.4 on 2022-05-08 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TreeAPI', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tree',
            name='user',
        ),
    ]
