# Generated by Django 3.2.3 on 2022-02-14 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eadogbeapp', '0043_alter_semaine_num_semaine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paiement_mise',
            name='nom_adhérent',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='eadogbeapp.adherent'),
        ),
    ]
