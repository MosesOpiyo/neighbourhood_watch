# Generated by Django 3.2.9 on 2021-11-05 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20211105_0805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='descrition',
            new_name='description',
        ),
    ]