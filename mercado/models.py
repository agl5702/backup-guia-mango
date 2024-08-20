from django.db import models

# Create your models here.
class TipoMercado(models.Model):
    name = models.CharField('Nombre del tipo de mercado',max_length=45)
    description = models.TextField('Descripción del tipo de mercado',max_length=1000)

    class Meta:
        db_table = 'Tipo_Mercado'
        verbose_name_plural = 'Tipos de mercados'

    def __str__(self):
        return self.name
    