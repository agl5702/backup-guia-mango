from django.db import models
from django.conf import settings
from variedad_mango.models import VariedadMango
from analisis_suelo.models import AnalisisSuelo
from herramientas_agricultura_precision.models import Herramientas,TipoMercado
from tipo_siembra.models import TipoSiembra
from django.contrib.auth import get_user_model  
from django.db.models.signals import pre_save
from django.dispatch import receiver

UserModel = get_user_model()

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
    state = models.ForeignKey(AnalisisSuelo, on_delete=models.CASCADE,editable=False) # Aptitud del suelo
    sowing_type=models.ForeignKey(TipoSiembra, on_delete=models.CASCADE) # Tipo de siembra
    tools = models.ForeignKey(Herramientas, on_delete=models.CASCADE)
    usuario = models.ForeignKey(UserModel, on_delete=models.CASCADE,default=get_user_model())    # usuario --- añadir

    class Meta:
        db_table ='Cultivos'
        verbose_name_plural = "Cultivos"

    def __str__(self):
        return self.name