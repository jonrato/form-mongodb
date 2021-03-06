# Generated by Django 3.2.7 on 2021-09-13 22:37

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0005_auto_20210913_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='anexos',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='uploads'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='areas_intervencao',
            field=models.CharField(choices=[('A3', 'AREA 3'), ('A1', 'AREA 1'), ('A2', 'AREA 2'), ('A4', 'AREA 4')], max_length=2),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='desc_det_proj',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='uploads'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='distrito_escola',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=1),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='fotografia_passe',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='uploads'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='n_participantes',
            field=models.CharField(choices=[('4', '4'), ('5', '5'), ('6', '6'), ('3', '3'), ('1', '1'), ('2', '2')], max_length=1),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='resumo_uma_pagina',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='uploads'), upload_to=''),
        ),
    ]
