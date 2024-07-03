from django.db import models

# Create your models here.
class Nutrientes(models.Model):
    level_choices = [
        ('BAJO','Bajo'),
        ('OPTIMO','Optimo'),
        ('ELEVADO','Elevado') 
    ]
    name = models.CharField('Nombre del nutriente',max_length=45)
    type_of_nutrient = models.CharField('Tipo de nutriente',max_length=45)
    description = models.CharField('Descripción del nutriente',max_length=100)
    levels= models.CharField(choices=level_choices,max_length=20)

    def __str__(self):
        return self.name
    
class pH(models.Model):
    level_choices= [
        ('BAJO','Bajo'),
        ('OPTIMO','Optimo'),
        ('ELEVADO','Elevado'),
    ]
    description = models.CharField(max_length=100)
    levels = models.CharField(choices=level_choices, max_length=20)

    def __str__(self):
        return self.description
    
class TipoTerreno(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class TipoSuelo(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=100)
    parameters = models.FloatField()
    nutrients = models.ForeignKey(Nutrientes, on_delete=models.CASCADE)
    ph = models.ForeignKey(pH, on_delete=models.CASCADE)
    type_of_terrain = models.ForeignKey(TipoTerreno, on_delete=models.CASCADE)

    def __str__(self):
        return self.name