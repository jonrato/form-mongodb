
from django.forms import ModelForm
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm, TextInput, EmailInput


class cadastrosForm(ModelForm):
    class Meta:
        model = cadastro
        fields = [
            'titulo_trabalho','areas_intervencao','prof_coordenador',
            'email_prof_coordenador','n_participantes','desc_det_proj','anexos','resumo_uma_pagina',
            'resumo_trabalho','nome','fotografia_passe','morada_completa','cod_postal','localidade',
            'sexo','nascimento','n_cartao_cidadao','n_id_fiscal','telefone','telemovel','email','escola_frequenta','pais','distrito_escola',
            'ano_frequenta','carreira_seguir','passatempo','termos_privacidade'
        ]

        widgets = {
            'titulo_trabalho': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'areas_intervencao': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                })
        }

def listar_cadastros(request):
    cadastrar = cadastro.objects.all()
    cadastros = {'lista': cadastrar}
    return render(request, 'list.html', cadastros)

def cadastro_new(request,template_name='cadastro_form.html'):
    form = cadastrosForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('sucess_form')
    return render(request,template_name, {'form':form})

def sucesso(request, template_name='sucesso.html'):
    return render(request, template_name)