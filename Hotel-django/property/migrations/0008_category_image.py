# Generated by Django 3.2.9 on 2021-11-15 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_reserve'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=123456789, upload_to='category/'),
            preserve_default=False,
        ),
    ]
