from django.contrib import admin

from apps.movimientos.animal.models import Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    search_fields = ['id','nombre']
    list_display = ['codigo','nombre']