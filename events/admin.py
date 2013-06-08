# encoding: utf-8

'''
admin.py é utilizada para registrar os models no admin
Aqui é possível definir quais os campos do model aparecerá na consulta dentro do admin
É possível também definir os campos que poderão servir como consulta
'''

from django.contrib import admin
from models import Event, Comment

def mark_private(modeladmin, request, queryset):
    '''Marca os eventos como privados'''
    queryset.update(public=False)
    modeladmin.message_user(request, u'Eventos atualizados com sucesso')

mark_private.short_description = u'Marcar como privado' #Modifica a descrição do campo no admin

class EventAdmin(admin.ModelAdmin):
    list_display  = ['name', 'type', 'public', 'comments_count'] #Coloca outros campos para serem visualizados no admin
    search_fields = ['name', 'description'] #Coloca campos como opção de pesquisa
    actions = [mark_private] #Adiciona a função de marcar privado ao admin

admin.site.register(Event, EventAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'event']
    search_fields = ['event__name'] #Atenção: o duplo underline serve para indicar que vai pegar dados de uma chave estrangeira


admin.site.register(Comment, CommentAdmin)

