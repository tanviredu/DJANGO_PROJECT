# Generated by Django 2.0 on 2019-05-14 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190514_0532'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='department',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='doctor',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
