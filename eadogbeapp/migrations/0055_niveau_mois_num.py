# Generated by Django 3.2.3 on 2022-02-15 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eadogbeapp', '0054_auto_20220215_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='niveau',
            name='mois_num',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eadogbeapp.mois_adherent'),
        ),
    ]
