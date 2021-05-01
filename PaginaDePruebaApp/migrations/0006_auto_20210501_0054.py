# Generated by Django 3.1.7 on 2021-05-01 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaDePruebaApp', '0005_chofer'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruta',
            name='descripcion',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='chofer',
            name='telefono',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='ruta',
            unique_together={('origen', 'destino', 'descripcion')},
        ),
    ]
