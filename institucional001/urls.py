from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'institucional001.catalogo.views.index', name='index'),
    
    (r'^revistas/', include('institucional001.catalogo.urls')),
    (r'^contato/', include('institucional001.contato.urls')),
    
    
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