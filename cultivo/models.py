from django.db import models
from variedad_mango.models import VariedadMango, AptitudSuelo
from herramientas_agricultura_precision.models import HerAgri
from tipo_siembra.models import TipoSiembra

class Cultivo(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    harvest_date = models.DateTimeField()
    mango_variety = models.ForeignKey(VariedadMango, on_delete=models.CASCADE)
    state = models.ForeignKey(AptitudSuelo, on_delete=models.CASCADE) # Aptitud del suelo
    sowing_type=models.ForeignKey(TipoSiembra, on_delete=models.CASCADE) # Tipo de siembra
    her_agri = models.ForeignKey(HerAgri, on_delete=models.CASCADE)

    def __str__(self):
        return self.name