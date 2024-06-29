# Generated by Django 5.0.6 on 2024-06-23 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='productos/')),
                ('nombre', models.CharField(max_length=100)),
                ('texto', models.CharField(max_length=100)),
                ('precio', models.CharField(max_length=50)),
            ],
        ),
    ]
