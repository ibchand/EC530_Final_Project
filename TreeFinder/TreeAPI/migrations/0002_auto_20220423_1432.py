# Generated by Django 3.2.12 on 2022-04-23 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TreeAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tree_ID', models.UUIDField()),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('long', models.DecimalField(decimal_places=6, max_digits=9)),
                ('Type', models.CharField(max_length=50)),
                ('UserKey', models.UUIDField()),
            ],
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
    ]
