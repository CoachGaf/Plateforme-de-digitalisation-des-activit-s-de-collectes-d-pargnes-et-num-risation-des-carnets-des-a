# Generated by Django 3.2.3 on 2021-09-27 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eadogbeapp', '0020_auto_20210921_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Echeance_jour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.DateField(blank=True, null=True)),
                ('nom_mois', models.CharField(blank=True, max_length=255, null=True)),
                ('mois_échéance', models.CharField(blank=True, max_length=255, null=True)),
                ('montant_penalité', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('payer_oui', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Echeance_mois',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_mois', models.IntegerField(blank=True, null=True)),
                ('nom_mois', models.CharField(blank=True, max_length=255, null=True)),
                ('date_debut_mois', models.DateField(blank=True, null=True)),
                ('date_fin_mois', models.DateField(blank=True, null=True)),
                ('montant_penalité', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('payer_oui', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Echeance_semaine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_semaine', models.IntegerField(blank=True, null=True)),
                ('nom_mois', models.CharField(blank=True, max_length=255, null=True)),
                ('date_debut_semaine', models.DateField(blank=True, null=True)),
                ('date_fin_semaine', models.DateField(blank=True, null=True)),
                ('montant_penalité', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('payer_oui', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paiement_echeance_jour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_souscription', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('jour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eadogbeapp.echeance_jour')),
                ('nom_adhérent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paiement_echeance_mois',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_souscription', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('nom_adhérent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('numero_mois', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eadogbeapp.echeance_mois')),
            ],
        ),
        migrations.CreateModel(
            name='Paiement_echeance_semaine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_souscription', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('nom_adhérent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('numero_semaine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eadogbeapp.echeance_semaine')),
            ],
        ),
        migrations.CreateModel(
            name='PenaliteUserJour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_penalité', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('adhérent', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('jour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eadogbeapp.echeance_jour')),
            ],
        ),
        migrations.CreateModel(
            name='PenaliteUserMois',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_penalité', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('adhérent', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('mois', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eadogbeapp.echeance_mois')),
            ],
        ),
        migrations.CreateModel(
            name='PenaliteUserSemaine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_penalité', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('adhérent', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('mois', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eadogbeapp.echeance_semaine')),
            ],
        ),
        migrations.RemoveField(
            model_name='paiement',
            name='nom_adhérent',
        ),
        migrations.RemoveField(
            model_name='paiement',
            name='nom_échéance',
        ),
        migrations.RemoveField(
            model_name='recu',
            name='nom_échéance',
        ),
        migrations.RemoveField(
            model_name='tontineadogbe',
            name='fréquence_paiement_tontine',
        ),
        migrations.AddField(
            model_name='groupeadogbe',
            name='fréquence_paiement_tontine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eadogbeapp.frequence'),
        ),
        migrations.AddField(
            model_name='groupeadogbe',
            name='nom_mois',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Echeance',
        ),
        migrations.DeleteModel(
            name='Paiement',
        ),
    ]