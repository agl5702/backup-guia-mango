from django.db import models

# Modelos de los tipos de siembra
class TipoSiembra(models.Model):
    name = models.CharField('Tipo de siembra', max_length=45)
    description = models.TextField('Descripción', max_length=1000)

    class Meta:
        db_table = 'Tipo_Siembra'
        verbose_name_plural = 'Tipos de siembra'
    
    def __str__(self):
        return self.name