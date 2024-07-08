from django.db import models
from variedad_mango.models import AnalisisSuelo

class AnalisisFoliar(models.Model):
    # Eliminar choices

    #eliminar choices
    nutrient = models.CharField(max_length=45)
    soil_analysis = models.ForeignKey(AnalisisSuelo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Analisis_Foliar'
        verbose_name_plural = 'Análisis Foliar'