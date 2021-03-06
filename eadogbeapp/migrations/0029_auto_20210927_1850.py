# Generated by Django 3.2.3 on 2021-09-27 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eadogbeapp', '0028_auto_20210927_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paiement_echeance_jour',
            name='nom_adhérent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eadogbeapp.adherent'),
        ),
        migrations.AlterField(
            model_name='penaliteuserjour',
            name='adhérent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eadogbeapp.adherent'),
        ),
        migrations.AlterField(
            model_name='penaliteusermois',
            name='adhérent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eadogbeapp.adherent'),
        ),
        migrations.AlterField(
            model_name='penaliteusersemaine',
            name='adhérent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eadogbeapp.adherent'),
        ),
        migrations.CreateModel(
            name='Carnet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_carnet', models.IntegerField()),
                ('adhérent', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eadogbeapp.adherent')),
            ],
        ),
    ]
