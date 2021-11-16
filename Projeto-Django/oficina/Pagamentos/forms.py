from django import forms
from django.contrib.admin.widgets import AdminDateWidget


class ContaReceberFormAdmin(forms.ModelForm):
    DataVencimento = forms.DateField(widget=AdminDateWidget(attrs={'class': "data vDateField"}), label="Data de Vencimento")


class ContaPagarFormAdmin(forms.ModelForm):
    DataVencimento = forms.DateField(widget=AdminDateWidget(attrs={'class': "data vDateField"}), label="Data de Vencimento")