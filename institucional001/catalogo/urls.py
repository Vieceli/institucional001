from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template
admin.autodiscover()

urlpatterns = patterns('',
    
  
    
    url(r'^(?P<cidade_slug>\w+)/$', 'institucional001.catalogo.views.cidade_index', name='cidade_index'),
    url(r'^(?P<cidade_slug>\w+)/(?P<slug>[-\w]+)/$', 'institucional001.catalogo.views.revista_flash',
        name='revista_flash'),
)
            #    url(r'^(?P<cidade_slug>\w+)/assinar/$', 'massive.engine.views.inscricao_cidade',
#        name='city_subscribe'),
#                                     
#    url(r'^(?P<cidade_slug>\w+)/(?P<oferta_slug>[-\w]+)/$',
#        'massive.engine.views.oferta_detalhe', name='oferta_detalhe'),
#                                     
#    url(r'^(?P<cidade_slug>\w+)/(?P<oferta_slug>[-\w]+)/(?P<quantidade>\d+)/checkout/completo/$',
#        'massive.engine.views.oferta_checkout_complete', name='oferta_checkout_complete'),
#                                     
#    url(r'^(?P<cidade_slug>\w+)/(?P<oferta_slug>[-\w]+)/comprar/$',
#        'massive.engine.views.oferta_checkout', name='oferta_checkout'),
                        