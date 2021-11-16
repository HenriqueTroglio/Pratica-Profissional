from django.contrib import admin
from .models import Marca, Categoria, Produto


class MarcaAdmin(admin.ModelAdmin):
    list_display = ['Id', 'Descricao']
    list_display_link = ['Id', 'Descricao']
    search_fields = ['Id', 'Descricao']


admin.site.register(Marca, MarcaAdmin)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['Id', 'Descricao']
    list_display_link = ['Id', 'Descricao']
    search_fields = ['Id', 'Descricao']


admin.site.register(Categoria, CategoriaAdmin)


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['Id', 'Descricao', 'Marca', 'Categoria']
    list_display_link = ['Id', 'Descricao']
    search_fields = ['Id', 'Descricao', 'Marca', 'Categoria']
    autocomplete_fields = ['Marca', 'Categoria']


admin.site.register(Produto, ProdutoAdmin)


# Register your models here.
