# Generated by Django 2.2.1 on 2019-06-06 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtors',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
