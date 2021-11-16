from django.contrib import admin
from .models import FormaPagamento, Parcela, CondicaoPagamento, ContaPagar, ContaReceber
from .forms import ContaPagarFormAdmin, ContaReceberFormAdmin


class FormaPagamentoAdmin(admin.ModelAdmin):
    list_display = ['Id', 'Descricao']
    list_display_link = ['Id', 'Descricao']
    search_fields = ['Id', 'Descricao']


admin.site.register(FormaPagamento, FormaPagamentoAdmin)


# class ParcelaAdmin(admin.ModelAdmin):
#     list_display = ['Id', 'Descricao']
#     list_display_link = ['Id', 'Descricao']
#     search_fields = ['Id', 'Descricao']
#
#
# admin.site.register(Parcela, ParcelaAdmin)

class ParcelaAdminInline(admin.TabularInline):
    model = Parcela
    extra = 0

class CondicaoPagamentoAdmin(admin.ModelAdmin):
    list_display = ['Id', 'Descricao']
    list_display_link = ['Id', 'Descricao']
    search_fields = ['Id', 'Descricao']
    inlines = (ParcelaAdminInline, )


admin.site.register(CondicaoPagamento, CondicaoPagamentoAdmin)

class ContaPagarAdmin(admin.ModelAdmin):
    list_display = ['Id', 'Descricao', 'Pago']
    list_display_link = ['Id', 'Descricao']
    search_fields = ['Id', 'Descricao', 'Pago']
    list_editable = ['Pago']
    form = ContaPagarFormAdmin


admin.site.register(ContaPagar, ContaPagarAdmin)

class ContaReceberAdmin(admin.ModelAdmin):
    list_display = ['Id', 'Descricao', 'Pago']
    list_display_link = ['Id', 'Descricao']
    search_fields = ['Id', 'Descricao', 'Pago']
    list_editable = ['Pago']
    form = ContaReceberFormAdmin


admin.site.register(ContaReceber, ContaReceberAdmin)