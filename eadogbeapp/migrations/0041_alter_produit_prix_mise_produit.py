# Generated by Django 3.2.3 on 2022-02-12 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eadogbeapp', '0040_auto_20220212_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='prix_mise_produit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
