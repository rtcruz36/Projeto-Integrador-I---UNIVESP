from django.contrib import admin

from .models import Medicamento, SaidaMedicamento

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'lote', 'validade', 'quantidade', 'tipo', 'esta_vencido', 'vencimento_proximo')
    list_filter = ('tipo',)
    search_fields = ('nome', 'lote')

@admin.register(SaidaMedicamento)
class SaidaMedicamentoAdmin(admin.ModelAdmin):
    list_display = ('medicamento', 'quantidade', 'data_saida', 'destino', 'foi_para_emergencia')
    list_filter = ('foi_para_emergencia',)
    search_fields = ('medicamento__nome', 'destino')