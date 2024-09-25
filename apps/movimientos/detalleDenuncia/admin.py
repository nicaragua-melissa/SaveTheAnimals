from django.contrib import admin

from apps.movimientos.detalleDenuncia.models import DetalleDenuncia

@admin.register(DetalleDenuncia)
class DetalleDenunciaAdmin(admin.ModelAdmin):
    search_fields = ['id','codigo']
    list_display = ['codigo']