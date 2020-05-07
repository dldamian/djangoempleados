from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.
admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'primer_nombre',
        'apellidos',
        'departamento',
        'trabajo',
        'nombre_completo',
        'id',
    )

    def nombre_completo(self, obj):
        return obj.primer_nombre + ' ' + obj.apellidos

    search_fields = ('primer_nombre',)
    list_filter = ('trabajo', 'habilidad','departamento')
    filter_horizontal = ('habilidad',)

admin.site.register(Empleado, EmpleadoAdmin)
