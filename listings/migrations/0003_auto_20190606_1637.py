# Generated by Django 2.2.1 on 2019-06-06 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20190602_0947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='descrition',
            new_name='description',
        ),
    ]