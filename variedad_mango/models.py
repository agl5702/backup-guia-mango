from django.db import models
from suelo.models import TipoSuelo
from tipo_siembra.models import TipoSiembra
from herramientas_agricultura_precision.models import TipoMercado


# Modelos de Variedad de mango y análisis del suelo
class VariedadMango(models.Model):

    name = models.CharField(max_length=45)
    description = models.TextField()
    soil_type = models.ForeignKey(TipoSuelo, on_delete=models.CASCADE)
    sowing_type = models.ForeignKey(TipoSiembra, on_delete=models.CASCADE)
    # change
    type_of_market = models.ManyToManyField(TipoMercado)

    class Meta:
        db_table='Variedad_mango'
        verbose_name_plural = 'Variedades de mango'

    def __str__(self):
        return self.name