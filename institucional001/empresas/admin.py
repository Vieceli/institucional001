# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Empresa
from institucional001.empresas.forms import EmpresaAdminForm
from django.forms import TextInput, Textarea 
#class CommentInline(admin.TabularInline):
#    model = models.Comment

class EmpresaAdmin(admin.ModelAdmin):
    """admin class"""
    fieldsets = (
                    (None, 
                     {
                        'fields': ('nome', 'proprietario', 'endereco', 
                                   'telefone', 'status', 'historico','ativo')
                     }
                     ),
                    ('Advanced options', 
                     {
                        'classes': ('collapse',),
                        'fields': ('mensagem', 'slug')
                      }
                     ),
                 )
    
    form = EmpresaAdminForm 
    
    radio_fields = {'status':admin.VERTICAL}

    list_filter = ('ativo', 'status','usuario')
    list_display = ['nome', 'status', 'telefone', 'endereco', 'usuario']
    list_per_page = 100
    search_fields = ['nome']
    prepopulated_fields = {
        'slug': ( 'nome', )
        
    }
    exclude = ('usuario',)
    
#    def save_formset(self, request, form, formset, change):
#        instances = formset.save(commit=False)
#        for instance in instances:
#            instance.usuario = request.username
#            instance.save()
#        formset.save_m2m()
#        
#    def save_model(self, request, obj, form, change):
#        data = obj.historico
#
#        items = [x for x in data.split('\n') if x and not x.isspace()]
#        for item in items:
#            Empresa.objects.create(historico=item)

    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()
        
    def queryset(self, request):
        qs=self.model._default_manager.filter(usuario=request.user)
        
        return qs



admin.site.register(Empresa, EmpresaAdmin)
