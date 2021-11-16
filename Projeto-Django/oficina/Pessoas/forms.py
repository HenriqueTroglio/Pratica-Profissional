from django import forms
from django.contrib.admin.widgets import AdminDateWidget


class ClienteFormAdmin(forms.ModelForm):
    CPF = forms.CharField(widget=forms.TextInput(attrs={'class': "cpf"}), label="CPF")
    DataNascimento = forms.DateField(widget=AdminDateWidget(attrs={'class': "data vDateField"}), label="Data de Nascimento")
    CEP = forms.CharField(widget=forms.TextInput(attrs={'class': "cep"}), label="CEP")
    Telefone = forms.CharField(widget=forms.TextInput(attrs={'class': "telefone"}), label="Telefone")


class FornecedorFormAdmin(forms.ModelForm):
    CNPJ = forms.CharField(widget=forms.TextInput(attrs={'class': "cnpj"}), label="CNPJ")
    CEP = forms.CharField(widget=forms.TextInput(attrs={'class': "cep"}), label="CEP")
    Telefone = forms.CharField(widget=forms.TextInput(attrs={'class': "telefone"}), label="Telefone")