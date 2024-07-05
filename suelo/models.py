from django.db import models

# Create your models here.
class FertilidadSuelo(models.Model):
    level_choices = [
        ('MUY BAJO','Muy Bajo'),
        ('BAJO','Bajo'),
        ('MODERADO','Moderado'),
        ('ALTO','Alto') 
    ]
    name = models.CharField('Nombre del nutriente',max_length=45)
    type_of_nutrient = models.CharField('Tipo de nutriente',max_length=45)
    description = models.CharField('Descripción del nutriente',max_length=500)
    level= models.CharField(choices=level_choices,max_length=20)
    value =models.FloatField()

    class Meta:
        verbose_name_plural = 'FertilidadSuelo'
    def __str__(self):
        return self.name
    
class pH(models.Model):
    level_choices= [
        ('BAJO','Bajo'),
        ('OPTIMO','Optimo'),
        ('ELEVADO','Elevado'),
    ]
    description = models.CharField(max_length=500)
    level = models.CharField(choices=level_choices, max_length=20)

    class Meta:
        verbose_name_plural = 'pH'
    def __str__(self):
        return self.description
    
class TipoTerreno(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = 'Tipos de terrenos'

    def __str__(self):
        return self.name
    
class TipoSuelo(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=500)
    nutrients = models.ForeignKey(FertilidadSuelo, on_delete=models.CASCADE)
    ph = models.ForeignKey(pH, on_delete=models.CASCADE)
    type_of_terrain = models.ForeignKey(TipoTerreno, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Tipos de suelos'

    def __str__(self):
        return self.name