# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django import forms
# Create your models here.
STATUS = (
        ('P', u'Prospecção'),
        ('A', u'Agendamento'),
        ('N', u'Negociação'),
        ('R', u'Retornar'),
        ('E', u'Proxima Edição'),
        ('F', u'Contrato Fechado'),
        ('C', u'Contrato Cancelado'),
        
    )
class Empresa(models.Model):
    nome = models.CharField(blank=False,max_length=50)
    proprietario = models.CharField(blank=False,max_length=50)
    endereco = models.CharField(blank=False,max_length=100)
    telefone = models.CharField(blank=False,max_length=50)
    historico = models.TextField(blank=False,max_length=200,)
    status = models.CharField(max_length=1, choices=STATUS, )
    mensagem = models.CharField(blank=True,max_length=250,)
    slug = models.SlugField(db_index=True)
    usuario = models.ForeignKey(User)
    ativo = models.BooleanField(default=True, db_index=True)
    data_publicacao       = models.DateTimeField(blank=True, editable=False, null=True, auto_now_add=True)
    data_modificacao      = models.DateTimeField(blank=True, editable=False, null=True, auto_now=True)
    data_exclusao         = models.DateTimeField(blank=True, editable=False, null=True)

    class Meta:
        db_table = 'empresas'
        ordering = ['-nome']
        verbose_name = _('Empresa')
        verbose_name_plural = _('Empresas')
        
    def __unicode__(self):
        return self.nome
    
    @models.permalink
    def get_absolute_url(self):
        return (u'empresa_nome', (), { u'empresa_nome': self.nome })
    
#    def save_model(self, request, obj, form, change):
#        data = obj.nome
#
#        items = [x for x in data.split('\n') if x and not x.isspace()]
#        for item in items:
#            Empresa.objects.create(nome=item)

    