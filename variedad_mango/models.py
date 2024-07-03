from django.db import models
from nutrientes.models import TipoSuelo
from tipo_siembra.models import TipoSiembra
from herramientas_agricultura_precision.models import TipoMercado
from hectareas.models import Hectareas

class VariedadMango(models.Model):

    name = models.CharField(max_length=45)
    description = models.CharField(max_length=100)
    soil_type = models.ForeignKey(TipoSuelo, on_delete=models.CASCADE)
    sowing_type = models.ForeignKey(TipoSiembra, on_delete=models.CASCADE)
    type_of_market = models.ForeignKey(TipoMercado, on_delete=models.CASCADE)
    hectareas = models.ForeignKey(Hectareas, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class AptitudSuelo(models.Model):
    description = models.CharField(max_length=100)
    soil_type = models.ForeignKey(TipoSuelo, on_delete=models.CASCADE)

    def __str__(self):
        return self.description