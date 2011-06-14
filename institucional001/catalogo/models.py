from django.db import models
import datetime
#from tagging.fields import TagField
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _



REVISTA_MINI = 'revista_mini/'

class Cidade(models.Model):
    cidade = models.CharField(blank=False,max_length=50, unique=True)
    estado = models.CharField(blank=False,max_length=50, unique=True)
    slug = models.SlugField(db_index=True)
    ativo = models.BooleanField(default=True, db_index=True)

    class Meta:
        db_table = 'cidades'
        ordering = ['-cidade']
        verbose_name = _('Cidade')
        verbose_name_plural = _('Cidades')
        
    def __unicode__(self):
        return self.cidade
    
    @models.permalink
    def get_absolute_url(self):
        return (u'cidade_revista', (), { u'cidade_revista': self.cidade })

class Area(models.Model):
    cidade = models.ForeignKey(Cidade)
    area = models.CharField(blank=False,max_length=50, unique=True)
    slug = models.SlugField(db_index=True)
    ativo = models.BooleanField(default=True, db_index=True)

    class Meta:
        db_table = 'localizacoes'
        ordering = ['-cidade']
        verbose_name = _('Area')
        verbose_name_plural = _('Areas')
        
    def __unicode__(self):
        return self.area
    
    @models.permalink
    def get_absolute_url(self):
        return (u'area_revista', (), { u'area_revista': self.area })
    
TIPO_REVISTA = (
        ('C', 'Clipper Magazine'),
        ('H', 'Home e design'),
    )
class Revista(models.Model):
    """
    Actual services
    """
    class Meta:
        verbose_name = _('Revista')
        verbose_name_plural = _('Revista')

    #objects = _default_manager = RevistaManager()
    
    nome = models.CharField(verbose_name=_("Nome da Revista"), max_length=256)
    tipo = models.CharField(max_length=1, choices=TIPO_REVISTA)
    arquivo              = models.FileField(upload_to='revistas/')
    cidade                = models.ForeignKey(Cidade, related_name='Cidade')
    area                  = models.ForeignKey(Area, related_name='Areas')
    slug                   = models.SlugField(db_index=True)
    ativo              = models.BooleanField(default=True, db_index=True)
    estreando                = models.BooleanField(default=True, db_index=True)
    miniatura                   = models.ImageField(upload_to='revista_mini/', blank=True)
    tags                    = models.CharField(verbose_name=_("Tags"), max_length=256)
    meta_keywords = models.CharField("Meta Keywords", max_length=255,
                                     help_text=u'Conjunto delimitado por virgulas de palavras-chave para SEO meta tag')
    meta_description = models.CharField("Meta Description", max_length=255,
                                        help_text=u'Descricao da meta-tag')
    publicado_em            = models.DateTimeField(blank=True, auto_now_add=True, db_index=True)
    data_modificacao              = models.DateTimeField(blank=True, editable=False, null=True, auto_now=True)
    data_exclusao            = models.DateTimeField(blank=True, editable=False, null=True)

    def __unicode__(self):
        return self.nome

    def esta_expirado(self):
        agora = datetime.datetime.now()
        expira_em = self.publicado_em + datetime.timedelta(hours=self.duracao_da_oferta)

        if expira_em < agora :
            return True
        else:
            return False

    def get_absolute_url(self):
        return reverse('revista_detalhe', kwargs={'cidade_slug': self.cidade.slug, 'revista_slug': self.slug})
    
    
class Edicao(models.Model):
    class Meta:
        verbose_name = _('Edicao')
        verbose_name_plural = _('Edicoes')

    numero = models.IntegerField();
    nome       = models.CharField(max_length=20)
    descricao = models.CharField(max_length=60)
    data_publicacao              = models.DateTimeField(blank=True, editable=False, null=True, auto_now_add=True)
    data_modificacao              = models.DateTimeField(blank=True, editable=False, null=True, auto_now=True)
    data_exclusao            = models.DateTimeField(blank=True, editable=False, null=True)
    estreando = models.BooleanField(default=True, db_index=True)
    revistas = models.ManyToManyField(Revista)

    def __unicode__(self):
        return self.nome
    
    def revista_estreando(self):
        revista=Revista.objects.filter(ativo=True,estreando=True)
        return tuple(revista)
        
    class Admin:
        list_display = ( "numero", "nome", "descricao", "data_modificacao" )
        
class Depoimento(models.Model):
    """
    Actual services
    """
    class Meta:
        verbose_name = _('Depoimento')
        verbose_name_plural = _('Depoimentos')
    
    depoimento = models.CharField(verbose_name=_("Depoimento"), max_length=256)
    autor = models.CharField(verbose_name=_("Autor"), max_length=256)



