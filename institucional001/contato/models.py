from django.db import models

# Create your models here.
class Agenda_Visita(models.Model):
    nome = models.CharField(blank=False,max_length=50)
    empresa = models.CharField(blank=False,max_length=50)
    tipo_anuncio = models.CharField(blank=False,max_length=50)
    tipo_midia = models.CharField(blank=False,max_length=50)
    telefone = models.CharField(blank=True,max_length=50)
    email = models.EmailField()
    mensagem = models.CharField(blank=False,max_length=250)
