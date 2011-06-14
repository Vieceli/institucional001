from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Agende_Visita(models.Model):
    
    class Meta:
        verbose_name = _('Agende visita')
        verbose_name_plural = _('Agende visitas')
    
    nome = models.CharField(blank=False,max_length=50)
    empresa = models.CharField(blank=False,max_length=50)
    telefone = models.CharField(blank=True,max_length=50)
    email = models.EmailField()
    mensagem = models.CharField(blank=False,max_length=250)
    
    def __unicode__(self):
        return self.email
    
    
class Contato(models.Model):
    
    class Meta:
        verbose_name = _('Contato')
        verbose_name_plural = _('Contatos')
    
    nome = models.CharField(blank=False,max_length=50)
    empresa = models.CharField(blank=False,max_length=50)
    email = models.EmailField()
    mensagem = models.CharField(blank=False,max_length=250)
    
    def __unicode__(self):
        return self.email

CIDADES = (('Go', 'Goiania'),('An', 'Anapolis.'),)


class EmailInscricao(models.Model):
    
    class Meta:
        verbose_name = _('Receber Email')
        verbose_name_plural = _('Receber Email')

    email = models.EmailField(blank=True, help_text="Endereco de email")
    cidade = models.CharField(max_length=20, choices=CIDADES, default=CIDADES[0][0])
    ativo = models.BooleanField(default=True, db_index=True)

    def __unicode__(self):
        return self.email
    
    