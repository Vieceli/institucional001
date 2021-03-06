'''
Created on 18/04/2011

@author: jhoni
'''
from django import forms
from institucional001.contato.models import EmailInscricao, Contato
from gmapi.forms.widgets import GoogleMap
#from institucional001.contato.models import Contato, Agende_Visita, EmailInscricao

class MapForm(forms.Form):
    map = forms.Field(widget=GoogleMap(attrs={'width':410, 'height':210}))

CIDADES = (('Go', 'Goiania'),('An', 'Anapolis.'),)

class EmailForm(forms.Form):
    email = forms.EmailField(label=u'Endereco de email')
    cidade = forms.ChoiceField(choices=CIDADES)
    
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            EmailInscricao.objects.get(email=email)
        except EmailInscricao.DoesNotExist:
            return email
        raise forms.ValidationError('Email ja cadastrado')
    
class Contato_Form(forms.Form):
    nome = forms.CharField(label=u'Nome ')
    empresa = forms.CharField()
    email = forms.EmailField(label=u'Endereco de email')
    telefone = forms.CharField()
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'rows':'8', 'cols': '50'}))
    
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            EmailInscricao.objects.get(email=email)
        except EmailInscricao.DoesNotExist:
            return email
        raise forms.ValidationError('Email ja cadastrado')

