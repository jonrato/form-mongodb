
from django.conf import settings
from django.forms import ModelForm
from django.http.response import JsonResponse
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
            'localidade_escola',
            'ano_frequenta','carreira_seguir','passatempo','termos_privacidade'
        ]
    
        


def listar_cadastros(request):
    cadastrar = cadastro.objects.all()
    cadastros = {'lista': cadastrar}
    return render(request, 'list.html', cadastros)

def cadastro_new(request,template_name='cadastro_form.html'):
    
    form = cadastrosForm(request.POST , request.FILES)
    
    

    if form.is_valid():

        form.save()
        nome = form.data['nome']
        email = form.data['email']
        send_email_api(request, nome,email)
        return redirect('sucess_form')
    else:
        form = cadastrosForm(request.POST , request.FILES)
    return render(request,template_name, {'form':form})

def sucesso(request, template_name='sucesso.html'):
    return render(request, template_name)

#Send Email Confirmation Subscribe
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings

def send_email_api(request,nome,email):
    class Meta:
        model = cadastro
    send_email_from_app(nome,email)
    data = {
        'sucess': True,
        'message':'Sua Inscrição Foi Realizada Com Sucesso!!!'
    }
    return JsonResponse(data)

def send_email_from_app(nome,email):
    data = {
        'email':email
    }
    
    html_tpl_path='confirmation.html'
    context_data = {'name':nome}
    email_html_template = get_template(html_tpl_path).render(context_data)
    receiver_email = '{}'.format(data['email'])
    email_msg = EmailMessage('Bem-Vindo',
                                email_html_template, settings.APPLICATION_EMAIL,
                                [receiver_email],
                                reply_to=[settings.APPLICATION_EMAIL]
    )
    email_msg.content_subtype = 'html'
    email_msg.send(fail_silently=False)
#END Send Email Confirmation Subscribe


#Página Inicial
def index(request, template_name='index.html'):
    return render(request, template_name)

#END Página Inicial

#About

def about(request, template_name='about.html'):
    return render(request, template_name)
#END About

#Contact
def contact(request, template_name='contact.html'):
    return render(request, template_name)
#END Contact

#Galeria
def galeria(request, template_name='galeria.html'):
    return render(request, template_name)
#END Galeria

#Membros Fundadores
def membros_fundadores(request, template_name='membrosfundadores.html'):
    
    return render(request, template_name)
#END Membros Fundadores

#Missão
def missao(request, template_name='Missao.html'):
    
    return render(request, template_name)
#End Missão

#Organograma
def organograma(request, template_name='Organigrama.html'):
    
    return render(request, template_name)

#END Organograma

#Regulamento
def regulamento(request, template_name='regulamento.html'):
    
    return render(request, template_name)
#END Regulamento

#Valores
def valores(request, template_name='Valores.html'):
    
    return render(request, template_name)
#END Valores

#Vantages
def vantagens(request, template_name='vantagens.html'):
    
    return render(request, template_name)
#END Vantages

#Visão
def visao(request, template_name='Visao.html'):
    
    return render(request, template_name)
#END Visão

#Blog Detail 1
def blog_1(request, template_name='blog_detail1.html'):

    return render(request, template_name)
#END Blog Detail 1

#Blog Detail 2
def blog_2(request, template_name='blog_detail2.html'):

    return render(request, template_name)
#END Blog Detail 2