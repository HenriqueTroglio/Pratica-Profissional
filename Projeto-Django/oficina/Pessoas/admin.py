from django.contrib import admin
from .models import Cliente, Fornecedor, Cargo, Funcionario
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .forms import ClienteFormAdmin, FornecedorFormAdmin


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['Id', 'Nome', 'Email']
    list_display_link = ['Id', 'Nome']
    search_fields = ['Id', 'Nome', 'Email']
    form = ClienteFormAdmin


admin.site.register(Cliente, ClienteAdmin)


class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['Id', 'NomeFantasia', 'Cidade', 'CNPJ']
    list_display_link = ['Id']
    search_fields = ['Id', 'NomeFantasia', 'RazaoSocial', 'CNPJ']
    form = FornecedorFormAdmin


admin.site.register(Fornecedor, FornecedorAdmin)


class CargoAdmin(admin.ModelAdmin):
    list_display = ['Id', 'Descricao']
    list_display_link = ['Id']
    search_fields = ['Id', 'Descricao']


admin.site.register(Cargo, CargoAdmin)


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class FuncionarioInline(admin.StackedInline):
    model = Funcionario
    can_delete = False
    verbose_name_plural = 'Funcionários'
    verbose_name = "Funcionário"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (FuncionarioInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
