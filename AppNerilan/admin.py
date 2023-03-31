from django.contrib import admin
from AppNerilan.models import *


# Register your models here.
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Finanzas)
admin.site.register(Avatar)

class EleccionAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'articulo', 'cantidad', 'fecha_eleccion']
    list_filter = ['cliente', 'fecha_eleccion']
    search_fields = ['cliente__nombre', 'articulo__nombre']

    def tienedeuda(self, obj):
        return obj.cliente.tienedeuda()

    def leido(self, obj):
        return obj.leido_por_admin()

    tienedeuda.boolean = True
    leido.boolean = True

admin.site.register(Articulo)
admin.site.register(Eleccion, EleccionAdmin)

