"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from formulario.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sendemail/', send_email_api),
    url(r'^list/', listar_cadastros, name='listar_cadastros'),
    url(r'^cadastro/', cadastro_new, name='cadastro_new'),
    url(r'^sucesso/', sucesso, name='sucess_form'),

    url(r'^$', index, name='index'),
    url(r'^about/', about, name='about'),
    url(r'^contact/', contact, name='contact'),
    url(r'^missao/', missao, name='missao'),
    url(r'^membrosfundadores/', membros_fundadores, name='membros_fundadores'),
    url(r'^organograma/', organograma, name='organograma'),
    url(r'^regulamento/', regulamento, name='regulamento'),
    url(r'^valores/', valores, name='valores'),
    url(r'^vantagens/', vantagens, name='vantagens'),
    url(r'^visao/', visao, name='visao'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)