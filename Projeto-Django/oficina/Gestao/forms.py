from django import forms
from django.contrib.admin.widgets import AdminDateWidget


class CompraFormAdmin(forms.ModelForm):
    DataCompra = forms.DateField(widget=AdminDateWidget(attrs={'class': "data vDateField"}), label="Data da Compra")
    DataRecebimento = forms.DateField(widget=AdminDateWidget(attrs={'class': "data vDateField"}), label="Data de Recebimento")