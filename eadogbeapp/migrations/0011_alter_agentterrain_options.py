# Generated by Django 3.2.3 on 2021-08-24 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eadogbeapp', '0010_auto_20210824_1623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agentterrain',
            options={'permissions': (('can_mark_user_agent', 'Set user as agent'),)},
        ),
    ]
