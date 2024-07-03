from django.db import models

# Create your models here.
class TipoSiembra(models.Model):
    name = models.CharField('Tipo de siembra', max_length=45)
    description = models.TextField('Descripción', max_length=100)

    class Meta:
        verbose_name_plural = 'Tipo de siembra'
    
    def __str__(self):
        return self.name