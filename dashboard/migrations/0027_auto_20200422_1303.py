# Generated by Django 3.0.3 on 2020-04-22 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0026_profile_state_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='city_location',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='state_location',
        ),
    ]
