# Generated by Django 3.2.3 on 2022-03-10 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eadogbeapp', '0061_auto_20220310_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carnet',
            name='agent',
        ),
    ]
