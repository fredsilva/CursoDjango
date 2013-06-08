# encoding: utf-8

from django.db import models
from django.core.urlresolvers import reverse

class Event(models.Model):

    TYPES_CHOICES = (
        (1, u'Workshop'),
        (2, u'Dojo'),
        (3, u'Palestra'),
    )

    name        = models.CharField(verbose_name=u'Nome', max_length=100)
    type        = models.IntegerField(verbose_name=u'Tipo do Evento', choices=TYPES_CHOICES)
    description = models.TextField(verbose_name=u'Descrição', blank=True)
    create_on   = models.DateTimeField(verbose_name=u'Criado em', auto_now_add=True)
    link        = models.URLField(verbose_name=u'Link',blank=True)
    public      = models.BooleanField(verbose_name=u'Público?', default=True)

    def comments_count(self):
        ''' Método que retorna a quantidade de comentários '''
        return self.comments.count() #comments é o related_name existente em Event

    comments_count.short_description = u'Número de Comentários' #Modifica a descrição do campo no admin

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('events_details', (), {'pk', self.pk})

    class Meta:
        verbose_name        = u'Evento'
        verbose_name_plural = u'Eventos'
        ordering            = ['name'] #ordena crescente ['-name'] #Ordena decrescente
        #db_table           = u'events' #Nome da tabela no Banco de dados

class Comment(models.Model):

    name       = models.CharField(verbose_name=u'Nome', max_length=100)
    email      = models.EmailField(verbose_name=u'E-mail')
    website    = models.URLField(verbose_name=u'Site', blank=True)
    event      = models.ForeignKey(Event, verbose_name=u'Evento', related_name='comments')
    text       = models.TextField(verbose_name=u'Texto')
    created_on = models.DateTimeField(verbose_name=u'Criado em', auto_now_add=True)

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name        = u'Comentário'
        verbose_name_plural = u'Comentários'
        ordering            = ['-created_on']
