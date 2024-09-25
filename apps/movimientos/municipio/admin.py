from django.contrib import admin

from apps.movimientos.municipio.models import Municipio

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    search_fields = ['id','codigo','descripcion']
    list_display = ['codigo','descripcion']
