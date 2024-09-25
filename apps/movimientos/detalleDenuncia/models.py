from django.db import models
from apps.movimientos.Denuncia.models import Denuncia
from apps.movimientos.animal.models import Animal

class DetalleDenuncia(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=5, unique=True)
    denuncia = models.ForeignKey(Denuncia, verbose_name= 'Denuncia', on_delete=models.PROTECT)
    animal = models.ForeignKey(Animal, verbose_name= 'Animal', on_delete=models.PROTECT)
    class Meta:
        verbose_name_plural = 'Detalles de Denuncia'

    def __str__(self):
        return f'{self.codigo}'