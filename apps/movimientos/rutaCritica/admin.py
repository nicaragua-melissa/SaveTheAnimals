from django.contrib import admin

from apps.movimientos.rutaCritica.models import RutaCritica

@admin.register(RutaCritica)
class RutaCriticaAdmin(admin.ModelAdmin):
    search_fields = ['id','codigo','descripcion']
    list_display = ['codigo','descripcion']