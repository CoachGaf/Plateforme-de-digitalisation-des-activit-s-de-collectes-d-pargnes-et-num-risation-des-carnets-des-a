# Generated by Django 3.2.3 on 2022-02-15 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eadogbeapp', '0053_mois_adherent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mois_adherent',
            old_name='num_mois',
            new_name='mois',
        ),
        migrations.RemoveField(
            model_name='niveau',
            name='mois',
        ),
    ]