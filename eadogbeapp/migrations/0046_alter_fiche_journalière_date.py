# Generated by Django 3.2.3 on 2022-02-14 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eadogbeapp', '0045_alter_paiement_mise_nom_adhérent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiche_journalière',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
