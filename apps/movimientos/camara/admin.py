from django.contrib import admin

from apps.movimientos.camara.models import Camara

@admin.register(Camara)
class CamaraAdmin(admin.ModelAdmin):
    search_fields = ['id','codigo']
    list_display = ['codigo','recording_Start','recording_End','estado']
