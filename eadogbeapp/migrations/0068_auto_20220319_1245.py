# Generated by Django 3.2.3 on 2022-03-19 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eadogbeapp', '0067_auto_20220316_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carnet',
            name='adhérent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='carnet', to='eadogbeapp.adherent'),
        ),
        migrations.AlterField(
            model_name='paiement_mise',
            name='nom_adhérent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paiement_mise', to='eadogbeapp.adherent'),
        ),
        migrations.AlterField(
            model_name='paiement_mise',
            name='num_carnet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='paiement_mise', to='eadogbeapp.carnet'),
        ),
    ]
