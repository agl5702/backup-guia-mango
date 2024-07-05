from django.db import models

# Create your models here.
class Hectareas(models.Model):

    amount=models.FloatField('Cantidad de Hectáreas')
    description = models.TextField('Descripción',max_length=500)
    number_trees= models.IntegerField('Cantidad de Árboles',default=0)

    class Meta:
        verbose_name_plural = 'Hectáreas'

    def __str__(self):
        return f"{self.amount}"
    
