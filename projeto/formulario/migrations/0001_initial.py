# Generated by Django 3.2.7 on 2021-09-13 19:02

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_trabalho', models.CharField(max_length=40)),
                ('areas_intervencao', models.CharField(choices=[('A3', 'AREA 3'), ('A1', 'AREA 1'), ('A4', 'AREA 4'), ('A2', 'AREA 2')], max_length=2)),
                ('prof_coordenador', models.CharField(max_length=50)),
                ('email_prof_coordenador', models.EmailField(max_length=254, null=True)),
                ('n_participantes', models.CharField(choices=[('4', '4'), ('3', '3'), ('5', '5'), ('6', '6'), ('2', '2'), ('1', '1')], max_length=1)),
                ('desc_det_proj', models.FileField(upload_to='uploads/')),
                ('anexos', models.FileField(upload_to='uploads/')),
                ('resumo_uma_pagina', models.FileField(upload_to='uploads/')),
                ('resumo_trabalho', models.CharField(max_length=1000)),
                ('nome', models.CharField(max_length=50)),
                ('fotografia_passe', models.FileField(upload_to='uploads/')),
                ('morada_completa', models.CharField(max_length=30)),
                ('cod_postal', models.CharField(max_length=30)),
                ('localidade', models.CharField(max_length=40)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('nascimento', models.DateField(null=True)),
                ('n_cartao_cidadao', models.CharField(max_length=50)),
                ('n_id_fiscal', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=30)),
                ('telemovel', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('escola_frequenta', models.CharField(max_length=50)),
                ('pais', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('distrito_escola', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=1)),
                ('localidade_escola', models.CharField(max_length=50)),
                ('ano_frequenta', models.CharField(max_length=10)),
                ('carreira_seguir', models.CharField(max_length=50)),
                ('passatempo', models.CharField(max_length=50)),
                ('termos_privacidade', models.BooleanField(default=False)),
            ],
        ),
    ]
