# Generated by Django 3.2.9 on 2021-11-15 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactdetails',
            old_name='Phone_number',
            new_name='phone_number',
        ),
    ]
