# Generated by Django 3.2.3 on 2021-10-07 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eadogbeapp', '0038_alter_paiement_echeance_semaine_numero_semaine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='echeance_mois',
            name='payer_oui',
        ),
        migrations.AddField(
            model_name='paiement_echeance_semaine',
            name='payer_oui',
            field=models.BooleanField(default=False),
        ),
    ]