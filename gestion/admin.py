from django.contrib import admin
from gestion.models import Arriendo, Equipo

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'presupuesto', 'creado')
    list_filter = ('presupuesto',)
    search_fields = ('nombre', 'descripcion')

class ArriendoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'stock', 'valor', 'equipo')
    search_fields = ('nombre', 'equipo__nombre')
    list_filter = ('equipo',)


admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Arriendo, ArriendoAdmin)
