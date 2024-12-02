from django.db import models

# Create your models here.
class Hectareas(models.Model):

    amount=models.FloatField('Cantidad de Hectáreas')
    description = models.TextField('Descripción',max_length=2000)
    number_trees= models.IntegerField('Cantidad de Árboles',default=0,editable=False)

    class Meta:
        db_table = 'Hectareas'
        verbose_name_plural = 'Hectáreas'

    def __str__(self):
        return f"{self.amount}"
    def save(self, *args, **kwargs):
        if self.amount:
            self.number_trees = int(self.amount * 200)  # Calcula el número de árboles basado en la cantidad de hectáreas
        else:
            self.number_trees = 0  # Si no hay cantidad definida, se establece en 0
        
        super().save(*args, **kwargs)
