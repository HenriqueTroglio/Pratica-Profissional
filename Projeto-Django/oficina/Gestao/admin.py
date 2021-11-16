from django.contrib import admin
from .models import Venda, ItemVenda, Compra, ItemCompra
from .forms import CompraFormAdmin
from django.db import transaction, IntegrityError
from django.db.models import Sum
from Pagamentos.models import CondicaoPagamento, ContaPagar, ContaReceber
import datetime


class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 0


class VendaAdmin(admin.ModelAdmin):
    list_display = ['NumeroNota', 'SerieNota', 'ModeloNota']
    list_display_link = ['NumeroNota']
    search_fields = ['NumeroNota', 'SerieNota', 'ModeloNota']
    inlines = [ItemVendaInline]

    def response_add(self, request, new_object):
        obj = self.after_saving_model_and_related_inlines(new_object)
        return super(VendaAdmin, self).response_add(request, obj)

    def response_change(self, request, obj):
        obj = self.after_saving_model_and_related_inlines(obj)
        return super(VendaAdmin, self).response_change(request, obj)

    @staticmethod
    def after_saving_model_and_related_inlines(obj):
        itensvendatotal = ItemVenda.objects.filter(Venda=obj.pk).aggregate(Sum('ValorTotal'))['ValorTotal__sum'] or 0.00

        try:
            with transaction.atomic():
                for parcela in obj.CondicaoPagamento.CondicaoPagamento_Parcela.all():
                    cr = ContaReceber(
                    Cliente = obj.Cliente,
                    DataVencimento = obj.DataVenda + datetime.timedelta(days=parcela.Dias),
                    Descricao = str(parcela.Numero) + " - " + parcela.FormaPagamento.Descricao + " - " + obj.Cliente.Nome ,
                    ValorInicial = itensvendatotal * (parcela.Percentual / 100),
                    ValorPago = 0,
                    CondicaoPagamento = parcela.CondicaoPagamento,
                    NumParcela = parcela.Numero,
                     )
                    cr.save()
        except IntegrityError:
            handle_exception()

        return obj


admin.site.register(Venda, VendaAdmin)


class ItemCompraInline(admin.TabularInline):
    model = ItemCompra
    extra = 0


class CompraAdmin(admin.ModelAdmin):
    list_display = ['NumeroNota', 'SerieNota', 'ModeloNota']
    list_display_link = ['NumeroNota']
    search_fields = ['NumeroNota', 'SerieNota', 'ModeloNota']
    inlines = [ItemCompraInline]
    form = CompraFormAdmin

    def response_add(self, request, new_object):
        obj = self.after_saving_model_and_related_inlines(new_object)
        return super(CompraAdmin, self).response_add(request, obj)

    def response_change(self, request, obj):
        obj = self.after_saving_model_and_related_inlines(obj)
        return super(CompraAdmin, self).response_change(request, obj)

    @staticmethod
    def after_saving_model_and_related_inlines(obj):
        itenscompratotal = ItemCompra.objects.filter(Compra=obj.pk).aggregate(Sum('ValorTotal'))['ValorTotal__sum'] or 0.00

        try:
            with transaction.atomic():
                for parcela in obj.CondicaoPagamento.CondicaoPagamento_Parcela.all():
                    cp = ContaPagar(
                    Fornecedor = obj.Fornecedor,
                    DataVencimento = obj.DataCompra + datetime.timedelta(days=parcela.Dias),
                    Descricao = str(parcela.Numero) + " - " + parcela.FormaPagamento.Descricao + " - " + obj.Fornecedor.NomeFantasia ,
                    ValorInicial = itenscompratotal * (parcela.Percentual / 100),
                    ValorPago = 0,
                    CondicaoPagamento = parcela.CondicaoPagamento,
                    NumParcela = parcela.Numero,
                     )
                    cp.save()
        except IntegrityError:
            handle_exception()

        return obj


admin.site.register(Compra, CompraAdmin)
