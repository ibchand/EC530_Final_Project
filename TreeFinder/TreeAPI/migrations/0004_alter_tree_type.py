# Generated by Django 4.0.4 on 2022-05-08 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TreeAPI', '0003_alter_tree_lat_alter_tree_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='Type',
            field=models.CharField(default='UNKNOWN', max_length=50),
        ),
    ]