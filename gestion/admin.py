from django.contrib import admin
from gestion.models import Arriendo, Equipo

def _formatear_monto(monto):
    return f"${monto:,}".replace(",", ".")

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'presupuesto_formateado', 'creado')
    list_filter = ('presupuesto',)
    search_fields = ('nombre', 'descripcion')

    @admin.display(description='Presupuesto')
    def presupuesto_formateado(self, obj):
        return _formatear_monto(obj.presupuesto)

class ArriendoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'stock', 'valor_formateado', 'equipo')
    search_fields = ('nombre', 'equipo__nombre')
    list_filter = ('equipo',)

    @admin.display(description='Valor')
    def valor_formateado(self, obj):
        return _formatear_monto(obj.valor)

admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Arriendo, ArriendoAdmin)
