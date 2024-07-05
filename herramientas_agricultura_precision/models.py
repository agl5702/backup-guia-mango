from django.db import models

# Create your models here.
class TipoMercado(models.Model):
    name = models.CharField('Nombre del tipo de mercado',max_length=45)
    description = models.TextField('Descripción del tipo de mercado',max_length=1000)

    class Meta:
        verbose_name_plural = 'Tipos de mercados'

    def __str__(self):
        return self.name
    
    
class Herramientas(models.Model):

    name = models.CharField('Nombre de la herramienta',max_length=145)
    description = models.TextField('Descripción de la herramienta',max_length=500)
    type_market = models.ManyToManyField(TipoMercado)

    class Meta:
        verbose_name_plural = 'Herramientas'

    def __str__(self):
        return self.name
    
