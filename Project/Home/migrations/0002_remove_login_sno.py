# Generated by Django 4.0.2 on 2022-06-19 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='sno',
        ),
    ]
