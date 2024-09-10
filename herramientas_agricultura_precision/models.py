from django.db import models
from mercado.models import TipoMercado
# Create your models here.

    
class Herramientas(models.Model):


    name = models.CharField('Nombre de la herramienta',max_length=145)
    description = models.TextField('Descripción de la herramienta',max_length=500)
    
    

    class Meta:
        db_table = 'Herramientas'
        verbose_name_plural = 'Herramientas'

    def __str__(self):
        return self.name
    
