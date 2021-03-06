# Generated by Django 3.2.3 on 2022-03-16 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eadogbeapp', '0066_remove_fiche_journalière_numero_fiche'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paiement_mise',
            name='mois',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paiement_mise',
            name='niveau',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paiement_mise',
            name='num_carnet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eadogbeapp.carnet'),
        ),
    ]
