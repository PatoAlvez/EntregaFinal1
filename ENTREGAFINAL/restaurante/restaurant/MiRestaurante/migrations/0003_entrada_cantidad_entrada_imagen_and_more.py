# Generated by Django 4.1.5 on 2023-03-16 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiRestaurante', '0002_remove_entrada_cantidad_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='cantidad',
            field=models.DateField(default=1),
        ),
        migrations.AddField(
            model_name='entrada',
            name='imagen',
            field=models.ImageField(default='/imagenes', upload_to=''),
        ),
        migrations.AddField(
            model_name='platoprincipal',
            name='cantidad',
            field=models.DateField(default=1),
        ),
        migrations.AddField(
            model_name='platoprincipal',
            name='imagen',
            field=models.ImageField(default='/imagenes', upload_to=''),
        ),
        migrations.AddField(
            model_name='postre',
            name='cantidad',
            field=models.DateField(default=1),
        ),
        migrations.AddField(
            model_name='postre',
            name='imagen',
            field=models.ImageField(default='/imagenes', upload_to=''),
        ),
    ]