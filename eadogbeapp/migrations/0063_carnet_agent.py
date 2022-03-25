# Generated by Django 3.2.3 on 2022-03-10 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eadogbeapp', '0062_remove_carnet_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='carnet',
            name='agent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
