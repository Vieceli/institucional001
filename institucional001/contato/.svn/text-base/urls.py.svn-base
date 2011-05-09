from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'institucional001.contato.views.agenda_visita_form', name='agenda_visita_form'),
    url(r'^agende_visita/$', 'institucional001.contato.views.agenda_visita_form', name='agenda_visita_form'),
    url(r'^agende_visita/agendado/$', direct_to_template, {'template': 'contato/sucesso.html'},
        name="contato_sucesso"),
)
                                     