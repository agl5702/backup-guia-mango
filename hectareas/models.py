from django.db import models

# Create your models here.
class Hectareas(models.Model):

    dimension=models.FloatField()
    description = models.TextField('Descripción',max_length=100)

    def __str__(self):
        return f"{self.dimension} hectáreas"
    
