# Generated by Django 3.1 on 2020-10-15 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200918_1040'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Story',
        ),
    ]
