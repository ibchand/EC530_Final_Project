# Generated by Django 4.0.4 on 2022-05-08 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TreeAPI', '0004_alter_tree_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='origin_lat',
            field=models.DecimalField(decimal_places=14, max_digits=17, null=True),
        ),
        migrations.AddField(
            model_name='journey',
            name='origin_long',
            field=models.DecimalField(decimal_places=14, max_digits=17, null=True),
        ),
    ]