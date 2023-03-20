# Generated by Django 4.1.5 on 2023-02-20 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plato', models.CharField(max_length=40)),
                ('cantidad', models.CharField(max_length=20)),
                ('bebida', models.CharField(max_length=40)),
                ('numero_de_mesa', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='PlatoPrincipal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plato', models.CharField(max_length=40)),
                ('bebida', models.CharField(max_length=40)),
                ('numero_de_mesa', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Postre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postres', models.CharField(max_length=40)),
                ('numero_de_mesa', models.CharField(max_length=5)),
            ],
        ),
    ]