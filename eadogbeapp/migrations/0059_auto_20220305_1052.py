# Generated by Django 3.2.3 on 2022-03-05 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eadogbeapp', '0058_auto_20220304_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='paiement_mise',
            name='achat_carte',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paiement_mise',
            name='nbr_mise',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paiement_mise',
            name='nouveau',
            field=models.BooleanField(default=False),
        ),
    ]
