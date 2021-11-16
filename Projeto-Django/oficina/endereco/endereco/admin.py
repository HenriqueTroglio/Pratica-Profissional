from django.contrib import admin
from .models import Pais, Estado, Cidade


class PaisAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'sigla']
    list_display_link = ['id', 'nome']
    search_fields = ['id', 'nome']
    # list_editable = ['ativo']


admin.site.register(Pais, PaisAdmin)


class EstadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'pais']
    list_display_link = ['id', 'nome', 'pais']
    search_fields = ['id', 'nome']
    # ordering = ['nome']
    # raw_id_fields = ['pais']
    autocomplete_fields = ['pais']


admin.site.register(Estado, EstadoAdmin)


class CidadeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'estado']
    list_display_link = ['id', 'nome', 'estado']
    search_fields = ['id', 'nome']
    autocomplete_fields = ['estado']


admin.site.register(Cidade, CidadeAdmin)
