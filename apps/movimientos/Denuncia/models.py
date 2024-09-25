from django.db import models
from apps.catalogos.tipoDenuncia.models import TipoDenuncia
from apps.movimientos.rutaCritica.models import RutaCritica

class Denuncia(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=5, unique=True)
    descripcion_persona = models.CharField(verbose_name='Descripción de persona involucrada', max_length=1000)
    descripcion_hechos = models.CharField(verbose_name='Descripción de los hechos', max_length=1000)
    direccion = models.CharField(verbose_name='Dirección', max_length=1000)
    zona = models.CharField(verbose_name='Zona', max_length=8)
    fecha = models.DateTimeField(verbose_name='Fecha')
    rutaCritica = models.ForeignKey(RutaCritica, verbose_name='Ruta Crítica', on_delete=models.PROTECT)
    tipoDenuncia = models.ForeignKey(TipoDenuncia, verbose_name= 'Tipo de Denuncia', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Denuncias'

    def __str__(self):
        return f'{self.codigo} - {self.fecha}'