# Generated by Django 3.2.3 on 2021-10-01 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eadogbeapp', '0033_alter_adherent_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adherent',
            options={'permissions': (('can_mark_user_adhérent', 'Set user as adhérent'), ('can_mark_adhérent_subscribe_échéance_jour', 'Set user as adhérent_subscribe_échéance_jour'), ('can_mark_adhérent_subscribe_échéance_semaine', 'Set user as adhérent_subscribe_échéance_semaine'), ('can_mark_adhérent_subscribe_échéance_mois', 'Set user as adhérent_subscribe_échéance_mois'))},
        ),
    ]
