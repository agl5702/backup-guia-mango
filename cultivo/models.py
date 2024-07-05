from django.db import models
from variedad_mango.models import VariedadMango, AptitudSuelo
from herramientas_agricultura_precision.models import Herramientas,TipoMercado
from tipo_siembra.models import TipoSiembra

class Cultivo(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=1000)
    start_date = models.DateField()
    harvest_date = models.DateField()
    hectareas= models.FloatField(default=2)
    # Nutrientes del suelo 
    #----------------------------------------------------------------
    mango_variety = models.ForeignKey(VariedadMango, on_delete=models.CASCADE)
    type_of_market = models.ForeignKey(TipoMercado, on_delete=models.CASCADE)
    state = models.ForeignKey(AptitudSuelo, on_delete=models.CASCADE,editable=False) # Aptitud del suelo
    sowing_type=models.ForeignKey(TipoSiembra, on_delete=models.CASCADE) # Tipo de siembra
    tools = models.ForeignKey(Herramientas, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Cultivos"

    def __str__(self):
        return self.name