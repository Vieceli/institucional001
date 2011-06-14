# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Cidade,Revista,Area,Edicao
from institucional001.contato.models import EmailInscricao

class AreaAdmin(admin.ModelAdmin):
    """Admin class"""
    prepopulated_fields = {
        'slug': ( 'area', )
    }

class CidadeAdmin(admin.ModelAdmin):
    """admin class"""
    list_display = ['cidade', 'estado', 'ativo']
    list_per_page = 100
    search_fields = ['cidade']
    prepopulated_fields = {
        'slug': ( 'cidade', )
    }

class EmailInscricaoAdmin(admin.ModelAdmin):
   """admin class"""

class RevistaAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ( 'nome', )
    }
    
class EdicaoAdmin(admin.ModelAdmin):
    """admin class"""
    

admin.site.register(Area, AreaAdmin)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(EmailInscricao, EmailInscricaoAdmin)
admin.site.register(Revista, RevistaAdmin)
admin.site.register(Edicao, EdicaoAdmin)


