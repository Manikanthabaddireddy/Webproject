# Generated by Django 4.0.2 on 2022-02-14 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0019_web_model_date_of_function'),
    ]

    operations = [
        migrations.AlterField(
            model_name='web_model',
            name='Date_Of_Function',
            field=models.DateField(),
        ),
    ]