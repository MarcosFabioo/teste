from django.contrib import admin
from .models import Funcionario, Dvd, Cidade, Cliente, Reserva

# Register your models here.
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome_funcionario', 'cpf', 'email')

@admin.register(Dvd)
class DvdAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'texto', 'valor')

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome_cidade', 'estado')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'email', 'telefone', 'cidade')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('data_reserva', 'data_entrega', 'valor')
