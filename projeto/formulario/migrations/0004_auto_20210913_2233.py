# Generated by Django 3.2.7 on 2021-09-13 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0003_auto_20210913_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='anexos',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='areas_intervencao',
            field=models.CharField(choices=[('A1', 'AREA 1'), ('A4', 'AREA 4'), ('A2', 'AREA 2'), ('A3', 'AREA 3')], max_length=2),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='desc_det_proj',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='distrito_escola',
            field=models.CharField(choices=[('B', 'B'), ('C', 'C'), ('A', 'A')], max_length=1),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='fotografia_passe',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='n_participantes',
            field=models.CharField(choices=[('5', '5'), ('2', '2'), ('1', '1'), ('4', '4'), ('6', '6'), ('3', '3')], max_length=1),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='resumo_uma_pagina',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='sexo',
            field=models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=1),
        ),
    ]
