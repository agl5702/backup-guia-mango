from django.db import models
from suelo.models import TipoSuelo,FertilidadSuelo,pH
from tipo_siembra.models import TipoSiembra
from herramientas_agricultura_precision.models import TipoMercado
from hectareas.models import Hectareas

class VariedadMango(models.Model):

    name = models.CharField(max_length=45)
    description = models.CharField(max_length=500)
    soil_type = models.ForeignKey(TipoSuelo, on_delete=models.CASCADE)
    sowing_type = models.ForeignKey(TipoSiembra, on_delete=models.CASCADE)
    type_of_market = models.ForeignKey(TipoMercado, on_delete=models.CASCADE)
    hectareas = models.ForeignKey(Hectareas, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Variedades de mango'

    def __str__(self):
        return self.name
    
class AptitudSuelo(models.Model):

    drainage_choices= [
        ('BUENO','Bueno'),
        ('LENTO','Lento'),
        ('EXCESIVO','Excesivo')
    ]

    name= models.CharField(max_length=45,blank=False,null=False)
    alert= models.BooleanField('Alerta',default=False)
    message = models.CharField(max_length=1000,blank=False,null=False)
    description = models.CharField(max_length=1000)
    drainage = models.CharField(choices=drainage_choices,null=False,max_length=255)
    ph = models.FloatField(null=False)
    nitrogen = models.FloatField(null=False)
    phosphorus = models.FloatField(null=False)
    potassium = models.FloatField(null=False)
    calcium = models.FloatField(null=False)
    magnesium = models.FloatField(null=False)
    sulfur = models.FloatField(null=False)
    iron = models.FloatField(null=False)
    manganese = models.FloatField(null=False)
    zinc = models.FloatField(null=False)
    copper = models.FloatField(null=False)
    molybdenum = models.FloatField(null=False)
    boron = models.FloatField(null=False)
    soil_type = models.ForeignKey(TipoSuelo, on_delete=models.CASCADE)
    soil_fertility= models.ForeignKey(FertilidadSuelo, on_delete=models.CASCADE)
    # usuario --- añadir
    
    class Meta:
        verbose_name_plural = 'Aptitudes del suelo'
    def __str__(self):
        return self.name