# Generated by Django 4.0.2 on 2022-02-19 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0034_remainder_model_remainder_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='remainder_model',
            old_name='remainder_Date',
            new_name='Remainder_Date',
        ),
        migrations.RenameField(
            model_name='remainder_model',
            old_name='remainder_Time',
            new_name='Remainder_Time',
        ),
    ]
