# Generated by Django 3.2.3 on 2021-09-27 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eadogbeapp', '0029_auto_20210927_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carnet',
            name='adhérent',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='eadogbeapp.adherent'),
        ),
    ]
