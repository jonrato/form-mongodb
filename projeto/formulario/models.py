from django.db import models
from django_countries.fields import CountryField
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='uploads')

class cadastro(models.Model):
    #dados do trabalho
    titulo_trabalho = models.CharField(max_length=40, verbose_name="Titulo do Trabalho")
    INTERVENCAO_CHOICES = {
        ('A1', 'AREA 1'),
        ('A2', 'AREA 2'),
        ('A3', 'AREA 3'),
        ('A4', 'AREA 4')
    }
    areas_intervencao = models.CharField(max_length=2, choices=INTERVENCAO_CHOICES, verbose_name="Áreas de Intervenção")
    prof_coordenador = models.CharField(max_length=50, verbose_name="Professor Coordenador")
    email_prof_coordenador = models.EmailField(null=True, verbose_name="Email do Professor Coordenador")
    NPARTICIPANTES = {
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
    }
    n_participantes = models.CharField(max_length=1, choices=NPARTICIPANTES, verbose_name="Nº de Participantes")
    desc_det_proj = models.FileField(storage=fs, verbose_name="Descrição Detalhada do Projeto")
    anexos = models.FileField(storage=fs, verbose_name="Anexos")
    resumo_uma_pagina = models.FileField(storage=fs,verbose_name="Resumo de 1 Página")
    resumo_trabalho = models.CharField(max_length=1000, verbose_name="Resumo do Trabalho")
    
    #dados do candidatos
    nome = models.CharField(max_length=50,verbose_name="Nome")
    fotografia_passe = models.FileField(storage=fs, verbose_name="Fotografia do Passe")
    morada_completa = models.CharField(max_length=30, verbose_name="Morada Completa")
    cod_postal = models.CharField(max_length=30, verbose_name="Código Postal")
    localidade = models.CharField(max_length=40,verbose_name="Localidade")
    SEXO_CHOICES = {
        ('M', 'Masculino'),
        ('F', 'Feminino')
    }
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES,verbose_name="Sexo")
    nascimento = models.DateField(null=True, verbose_name="Data de Nascimento")
    n_cartao_cidadao = models.CharField(max_length=50, verbose_name="Nº do Cartão Cidadão")
    n_id_fiscal = models.CharField(max_length=50, verbose_name="Nº do Id Fiscal")
    telefone = models.CharField(max_length=30, verbose_name="Telefone")
    telemovel = models.CharField(max_length=50,verbose_name="Telemovel")
    email = models.EmailField(null=True, verbose_name="Email")
    escola_frequenta = models.CharField(max_length=50,verbose_name="Escola/Universidade que Frequenta")
    pais = CountryField(blank=True, verbose_name="País")
    DISTRITO_ESCOLA_CHOICES = {
        ('A','A'),
        ('B','B'),
        ('C','C')
    }
    distrito_escola = models.CharField(max_length=1, choices=DISTRITO_ESCOLA_CHOICES, verbose_name="Distrito da Escola")
    localidade_escola = models.CharField(max_length=50, verbose_name="Localidade da Escola")
    ano_frequenta = models.CharField(max_length=10, verbose_name="Ano que Frequenta")
    carreira_seguir = models.CharField(max_length=50, verbose_name="Carreira a Seguir")
    passatempo = models.CharField(max_length=50, verbose_name="Passatempo")
    termos_privacidade = models.BooleanField(default=False, verbose_name="Li e Concordo com os Termos de Privacidade")

    def __str__(self):
        return self.nome
