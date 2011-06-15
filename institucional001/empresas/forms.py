'''
Created on 18/04/2011

@author: jhoni
'''
from django.forms.models import ModelForm
from django import forms
from institucional001.empresas.models import STATUS, Empresa


class EmpresaAdminForm(forms.ModelForm):
    #comentario = forms.CharField(widget=forms.TextInput())
    #status = forms.CharField(widget=forms.RadioSelect())
#    quantidade = forms.IntegerField(widget=forms.TextInput(attrs={'size':'2',
#                                    'value':'1', 'class':'quantidade', 'maxlength':'5'}),
#                                     error_messages={'invalido':'Coloque uma quantidade valida.'},
#                                     min_value=1)
#    produto_slug = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Empresa
