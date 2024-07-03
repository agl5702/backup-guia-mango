from django.db import models

# Create your models here.
class HerAgri(models.Model):

    name = models.CharField('Nombre de la herramienta',max_length=145)
    description = models.TextField('Descripción de la herramienta',max_length=100)

    def __str__(self):
        return self.name
    

class TipoMercado(models.Model):
    name = models.CharField('Nombre del tipo de mercado',max_length=45)
    description = models.TextField('Descripción del tipo de mercado',max_length=100)
    her_agri = models.ForeignKey(HerAgri,on_delete=models.CASCADE)

    def __str__(self):
        return self.name