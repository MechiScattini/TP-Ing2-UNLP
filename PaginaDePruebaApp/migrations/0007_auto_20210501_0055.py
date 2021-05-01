# Generated by Django 3.1.7 on 2021-05-01 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaDePruebaApp', '0006_auto_20210501_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='dni',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='clientegold',
            name='ahorro',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='descripcion',
            field=models.CharField(max_length=50),
        ),
    ]
