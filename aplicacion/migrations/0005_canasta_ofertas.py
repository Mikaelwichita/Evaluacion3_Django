# Generated by Django 5.0.6 on 2024-06-27 02:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_canasta_bandanas_canasta_collares_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='canasta',
            name='ofertas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.producto_ofertas'),
        ),
    ]
