# Generated by Django 4.0.2 on 2022-02-14 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0011_alter_web_model_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='web_model',
            name='Another_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]