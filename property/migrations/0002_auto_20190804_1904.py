# Generated by Django 2.2.4 on 2019-08-04 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='area',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
