# Generated by Django 3.2.3 on 2022-02-15 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eadogbeapp', '0048_remove_mise_agent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jours', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eadogbeapp.jours')),
                ('mois', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eadogbeapp.mois')),
            ],
        ),
    ]
