# Create your views here.
#from institucional001.contato.forms import Agenda_Visita_Form
from django.core.mail.message import EmailMessage
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from institucional001.contato.forms import Contato_Form, MapForm
from institucional001.contato.models import Contato
from institucional001.catalogo.views import cidade_index

#GeoIP
from django.contrib.gis.utils import GeoIP
from gmapi import maps

#def contato(request):
#    #Mapa
#    gmap = maps.Map(opts = {
#        'center': maps.LatLng('-34', '20'),
#        'mapTypeId': maps.MapTypeId.ROADMAP,
#        'zoom': 15,
#        'mapTypeControlOptions': {
#             'style': maps.MapTypeControlStyle.DROPDOWN_MENU
#        },
#    })
#    marker = maps.Marker(opts = {
#        'map': gmap,
#        'position': maps.LatLng('-34', '20'),
#    })
#    maps.event.addListener(marker, 'mouseover', 'myobj.markerOver')
#    maps.event.addListener(marker, 'mouseout', 'myobj.markerOut')
#    info = maps.InfoWindow({
#        'content': '<h3>'+'Clipper Magazine'+'</h3>'+
#                   '<p>Rua: '+'etc etc'+'</p>'+
#                   '<p>Telefone: '+'62 888992212'+'</p>',
#                   'disableAutoPan': False
#    })
#    info.open(gmap, marker)
#
#    #formulario de contato
#    if request.POST:
#        postdata = request.POST.copy()
#        form_contato = Contato_Form(postdata)
#        if form_contato.is_valid():
#            cad_contato=Contato()
#            cad_contato.nome=form_contato.cleaned_data['nome']
#            cad_contato.empresa=form_contato.cleaned_data['empresa']
#            cad_contato.email=form_contato.cleaned_data['email']
#            cad_contato.telefone = cad_contato.cleaned_data['telefone']
#            cad_contato.mensagem=form_contato.cleaned_data['mensagem']
#            cad_contato.save()
#            
#            mensagem_site=form_contato.cleaned_data['mensagem']
#            mensagem = "Ola\nO %s Mandou a seguinte mensagem:\n%s" %(cad_contato.nome,mensagem_site)
#            email = EmailMessage(cad_contato.mensagem,mensagem, to=['veiodruida@gmail.com'])
#            email.send()
#            
#            if request.is_ajax():
#                return render_to_response('contato/sucesso.html')
#            else:
#               return redirect('contato_sucesso')
#    else:
#        form_contato = Contato_Form()
#
#    context = {'form_mapa': MapForm(initial={'map': gmap}),
#               'form_contato': form_contato,
#              }
#    return render_to_response('contato/contato.html', context, context_instance=RequestContext(request))

    