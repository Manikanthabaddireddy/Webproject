# Generated by Django 4.0.2 on 2022-02-17 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0031_remainder_model_delete_remainder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='remainder_model',
            name='Date',
        ),
        migrations.AddField(
            model_name='remainder_model',
            name='Calling_status',
            field=models.CharField(blank=True, choices=[('call-back', 'call-back'), ('declined', 'declined')], max_length=20),
        ),
        migrations.AddField(
            model_name='remainder_model',
            name='Date_And_Time',
            field=models.DateTimeField(blank=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', null=True),
        ),
    ]
