from django.db import models
from analisis_suelo.models import AnalisisSuelo

class AnalisisFoliar(models.Model):
    level_choices = [
        ('BAJO','Bajo'),
        ('OPTIMO','Óptimo'),
        ('ELEVADO','Elevado'),
    ]

    #eliminar choices
    nutrient = models.CharField(max_length=45)
    soil_analysis = models.ForeignKey(AnalisisSuelo, on_delete=models.CASCADE)
    level= models.CharField('Nivel', choices=level_choices,max_length=10,default=0)
    class Meta:
        db_table = 'Analisis_Foliar'
        verbose_name_plural = 'Análisis Foliar'