from django.db import models

# Create your models here.
class Plaga(models.Model):
    nombre = models.CharField('Nombre de plaga',max_length=100)
    descripcion = models.TextField('Descripcion de plaga')
    imagen = models.ImageField('Imagen de plaga',upload_to='plagas/', null=True, blank=True)

    def __str__(self):
        
        return self.nombre

