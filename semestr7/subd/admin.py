from django.contrib import admin
from django.db.models import Count
from .model import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'fio']
    search_fields = ['id', 'fio']

admin.site.register(Client, ClientAdmin)


class FilialAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'phone']
    search_fields = ['id', 'name', 'address', 'phone']

admin.site.register(Filial, FilialAdmin)


class AgentAdmin(admin.ModelAdmin):
    list_display = ['id', 'fio', 'filial']
    search_fields = ['id', 'fio']

admin.site.register(Agent, AgentAdmin)


class ContractAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'type', 'amount', 'tariff', 'filial', 'client', 'agent']
    search_fields = ['id', 'amount']
    list_filter = ['type', 'date', 'filial']

admin.site.register(Contract, ContractAdmin)
