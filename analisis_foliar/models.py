from django.db import models
from variedad_mango.models import AnalisisSuelo

class AnalisisFoliar(models.Model):
    level_choices = [
        ('Bajo', 'Bajo'),
        ('Medio', 'Medio'),
        ('Suficiente', 'Suficiente'),
        ('Alto', 'Alto'),
        ('Exceso', 'Exceso'),
    ]
    level = models.CharField(max_length=10, choices=level_choices)
    nutrient = models.CharField(max_length=45)
    soil_analysis = models.ForeignKey(AnalisisSuelo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Analisis_Foliar'
        verbose_name_plural = 'Análisis Foliar'