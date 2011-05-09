'''
Created on 18/04/2011

@author: jhoni
'''
from django.forms.models import ModelForm
from django import forms
from institucional001.catalogo.models import EmailInscricao
from institucional001.contato.models import Agenda_Visita

class EmailForm(ModelForm):
    username = forms.CharField(max_length=30, label=u'Usuario')
    email = forms.EmailField(label=u'Endereco de email')
    
    class Meta:
        model = EmailInscricao
        
class Agenda_Visita_Form(forms.Form):
    nome = forms.CharField(label=u'Nome ')
    empresa = forms.CharField()
    tipo_anuncio = forms.CharField()
    tipo_midia = forms.CharField()
    telefone = forms.CharField()
    email = forms.EmailField(label=u'Endereco de email')
    mensagem = forms.CharField()
    
    class Meta:
        model = Agenda_Visita
