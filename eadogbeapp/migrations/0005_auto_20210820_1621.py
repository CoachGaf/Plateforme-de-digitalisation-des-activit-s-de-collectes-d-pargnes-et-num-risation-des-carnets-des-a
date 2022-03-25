# Generated by Django 3.2.3 on 2021-08-20 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eadogbeapp', '0004_auto_20210816_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adherent',
            name='adresse_mail_adhérent',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='adherent',
            name='email_de_notification',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='initiateur',
            name='adresse_email_initiateur',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='initiateur',
            name='email_de_notification',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
    ]