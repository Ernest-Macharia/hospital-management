# Generated by Django 2.2.1 on 2020-03-20 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_auto_20200321_0215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='receptionist',
        ),
    ]