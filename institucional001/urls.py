from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'institucional001.catalogo.views.index', name='index'),
    
    #(r'^revistas/', include('institucional001.catalogo.urls')),
    url(r'^(?P<cidade_slug>\w+)/$', 'institucional001.catalogo.views.cidade_index', name='cidade_index'),
    
    url(r'^(?P<cidade_slug>\w+)/revistas/$', 'institucional001.catalogo.views.revistas', name='revistas'),
    
    url(r'^(?P<cidade_slug>\w+)/contato/$', 'institucional001.catalogo.views.contato', name='contato'),
    
    url(r'^(?P<cidade_slug>\w+)/(?P<slug>[-\w]+)/$', 'institucional001.catalogo.views.revista_flash',
        name='revista_flash'),
    
    
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    # Static stuff (apache should serve this in production)
    (r'^(robots.txt)$', 'django.views.static.serve', {'document_root': '/var/www/massivecoupon/'}),
    
)

if settings.LOCAL:
    urlpatterns = urlpatterns + patterns('',
        ((r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT})),
        )
    

handler404 = 'institucional001.views.file_not_found_404'
handler500 = 'institucional001.views.server_error_500'
    
#                                     