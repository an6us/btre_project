# Generated by Django 2.2.1 on 2019-06-02 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.DecimalField(decimal_places=1, max_digits=20),
        ),
    ]
