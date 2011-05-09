# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from institucional001 import settings
from django.shortcuts import render_to_response, get_object_or_404, redirect
from institucional001.catalogo.models import Cidade, Revista
from django.template.context import RequestContext
from django.utils import simplejson
from django.core.mail import mail_admins
from django.core.mail.message import EmailMessage
from django.core.context_processors import csrf

def cidade_index(request, cidade_slug):
    cidade = get_object_or_404(Cidade, slug=cidade_slug)
    cidades_disponiveis = Cidade.objects.all()
    #revistas = Revista.objects.ativa_na_cidade(cidade)
    #revistas = get_object_or_404(Revista, cidade=cidade)
    revistas = Revista.objects.filter(cidade=cidade,ativo=True)
    estreando = Revista.objects.filter(cidade=cidade,ativo=True,estreando=True)[:8]
    meta_keywords = settings.META_KEYWORDS
    meta_description = settings.META_DESCRIPTION

    return render_to_response('index.html',locals(),context_instance=RequestContext(request),)

def index(request):
    return HttpResponseRedirect(settings.DEFAULT_CITY_SLUG)

def revista_flash(request,cidade_slug,nome):
    cidade = get_object_or_404(Cidade, slug=cidade_slug)
    cidades_disponiveis = Cidade.objects.all()
    revista = get_object_or_404(Revista, cidade=cidade, nome=nome)
    meta_keywords = revista.meta_keywords
    meta_description = revista.meta_description
    
    return render_to_response('revista/revista.html',locals(),context_instance=RequestContext(request),) 
    


    