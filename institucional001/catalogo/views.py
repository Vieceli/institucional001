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
from institucional001.contato.forms import EmailForm, Contato_Form, MapForm
from institucional001.contato.models import EmailInscricao, Contato
#GeoIP
from django.contrib.gis.utils import GeoIP
from gmapi import maps

def cidade_index(request, cidade_slug):
    cidade = get_object_or_404(Cidade, slug=cidade_slug)
    cidades_disponiveis = Cidade.objects.all()
    #revistas = Revista.objects.ativa_na_cidade(cidade)
    #revistas = get_object_or_404(Revista, cidade=cidade)
    revistas = Revista.objects.filter(cidade=cidade,ativo=True)
    estreando = Revista.objects.filter(cidade=cidade,ativo=True,estreando=True)[:8]
    meta_keywords = settings.META_KEYWORDS
    meta_description = settings.META_DESCRIPTION
                
    email_form = EmailForm()
    email_cadastrado = False  
    email_duplicado=False  
       
    if request.POST:
        postdata = request.POST.copy()
        email_form = EmailForm(postdata)
        if email_form.is_valid():
            cad_email=EmailInscricao()
            cad_email.email=email_form.cleaned_data['email']
            cidade=email_form.cleaned_data['cidade']
            cad_email.save()
            email_cadastrado = True

    return render_to_response('index.html',locals(),context_instance=RequestContext(request),)

def revistas(request, cidade_slug):
    cidade = get_object_or_404(Cidade, slug=cidade_slug)
    cidades_disponiveis = Cidade.objects.all()
    #revistas = Revista.objects.ativa_na_cidade(cidade)
    #revistas = get_object_or_404(Revista, cidade=cidade)
    revistas = Revista.objects.filter(cidade=cidade,ativo=True)
    estreando = Revista.objects.filter(cidade=cidade,ativo=True,estreando=True)[:8]
    meta_keywords = settings.META_KEYWORDS
    meta_description = settings.META_DESCRIPTION
    
    email_form = EmailForm()
    email_cadastrado = False  
    email_duplicado=False     
    if request.POST:
        postdata = request.POST.copy()
        email_form = EmailForm(postdata)
        if email_form.is_valid():
            cad_email=EmailInscricao()
            cad_email.email=email_form.cleaned_data['email']
            cidade=email_form.cleaned_data['cidade']
            cad_email.save()
            email_cadastrado = True
    
    return render_to_response('revista/revistas.html',locals(),context_instance=RequestContext(request),)
    

def index(request):
    return HttpResponseRedirect(settings.DEFAULT_CITY_SLUG)

def revista_flash(request,cidade_slug,slug): #slug eh a revista_slug
    cidade = get_object_or_404(Cidade, slug=cidade_slug)
    cidades_disponiveis = Cidade.objects.all()
    revista = get_object_or_404(Revista, cidade=cidade, slug=slug)
    meta_keywords = revista.meta_keywords
    meta_description = revista.meta_description
    
    email_form = EmailForm()
    email_cadastrado = False  
    email_duplicado=False     
    if request.POST:
        postdata = request.POST.copy()
        email_form = EmailForm(postdata)
        if email_form.is_valid():
            cad_email=EmailInscricao()
            cad_email.email=email_form.cleaned_data['email']
            cidade=email_form.cleaned_data['cidade']
            cad_email.save()
            email_cadastrado = True
    
    return render_to_response('revista/revista.html',locals(),context_instance=RequestContext(request),) 
    

def contato(request,cidade_slug):
    cidade = get_object_or_404(Cidade, slug=cidade_slug)
    cidades_disponiveis = Cidade.objects.all()
    #Mapa
    gmap = maps.Map(opts = {
        'center': maps.LatLng('-34', '20'),
        'mapTypeId': maps.MapTypeId.ROADMAP,
        'zoom': 15,
        'mapTypeControlOptions': {
             'style': maps.MapTypeControlStyle.DROPDOWN_MENU
        },
    })
    marker = maps.Marker(opts = {
        'map': gmap,
        'position': maps.LatLng('-34', '20'),
    })
    maps.event.addListener(marker, 'mouseover', 'myobj.markerOver')
    maps.event.addListener(marker, 'mouseout', 'myobj.markerOut')
    info = maps.InfoWindow({
        'content': '<h3>'+'Clipper Magazine'+'</h3>'+
                   '<p>Rua: '+'etc etc'+'</p>'+
                   '<p>Telefone: '+'62 888992212'+'</p>',
                   'disableAutoPan': False
    })
    info.open(gmap, marker)

    #formulario de contato
    if request.POST:
        postdata = request.POST.copy()
        form_contato = Contato_Form(postdata)
        if form_contato.is_valid():
            cad_contato=Contato()
            cad_contato.nome=form_contato.cleaned_data['nome']
            cad_contato.empresa=form_contato.cleaned_data['empresa']
            cad_contato.email=form_contato.cleaned_data['email']
            cad_contato.telefone = cad_contato.cleaned_data['telefone']
            cad_contato.mensagem=form_contato.cleaned_data['mensagem']
            cad_contato.save()
            
            mensagem_site=form_contato.cleaned_data['mensagem']
            mensagem = "Ola\nO %s Mandou a seguinte mensagem:\n%s" %(cad_contato.nome,mensagem_site)
            email = EmailMessage(cad_contato.mensagem,mensagem, to=['veiodruida@gmail.com'])
            email.send()
            
            if request.is_ajax():
                return render_to_response('contato/sucesso.html')
            else:
               return redirect('contato_sucesso')
    else:
        form_contato = Contato_Form()
    
    email_form = EmailForm()
    email_cadastrado = False       
    if request.POST:
        postdata = request.POST.copy()
        email_form = EmailForm(postdata)
        if email_form.is_valid():
            cad_email=EmailInscricao()
            cad_email.email=email_form.cleaned_data['email']
            cidade=email_form.cleaned_data['cidade']
            cad_email.save()
            email_cadastrado = True
            
    context = {'form_mapa': MapForm(initial={'map': gmap}),
               'email_form':email_form,
               'email_cadastrado':email_cadastrado,
               'form_contato': form_contato,
               'cidades_disponiveis':cidades_disponiveis,
               'cidade':cidade,
              }
    return render_to_response('contato/contato.html', context, context_instance=RequestContext(request))

def _cidade_cliente(request):
     #geo
    ip_address=request.META.get('REMOTE_ADDR') 
    g = GeoIP()
    #local_full_cliente = g.city(ip_address)
    local_full_cliente = g.city('201.22.164.216')
    cidade_cliente = local_full_cliente.get('city')
    uni = cidade_cliente.decode('cp1252')
    cidade_cliente = uni.encode('utf8')
    return cidade_cliente
    