# Generated by Django 5.1.3 on 2025-02-15 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vente',
            name='prix_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
