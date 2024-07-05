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
    level= models.CharField('Nivel del nutriente',choices=level_choices,max_length=20)
    value =models.FloatField('Valor del nutriente')

    class Meta:
        db_table='Fertilidad_suelo'
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
        db_table = 'ph'
        verbose_name_plural = 'pH'
    def __str__(self):
        return self.description
    
class TipoTerreno(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=500)

    class Meta:
        db_table = 'Tipo_terreno'
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
        db_table = 'tipo_suelo'
        verbose_name_plural = 'Tipos de suelos'

    def __str__(self):
        return self.name
    
class TexturaSuelo(models.Model):
    name_choices= [
        ('Arena', 'Arena'),
        ('Limo', 'Limo'),
        ('Arcilla', 'Arcilla'),
    ]
    name = models.CharField('Nombre de textura',max_length=20, choices=name_choices)
    value = models.FloatField()
    description = models.TextField('Descripción')

    class Meta:
        db_table = 'Textura_Suelo'
        verbose_name_plural = 'Texturas del suelo'
        
class DrenajeSuelo(models.Model):
    level_choices= [
        ('MALO','Malo'),
        ('BUENO','Bueno'),
        ('ADECUADO','Adecuado'),

    ]

    level = models.CharField('Nivel de drenaje', max_length=50, choices=level_choices)
    value = models.FloatField('Valor de referencia')
    infiltration_rate= models.FloatField('Tasa de infiltración')
    field_capacity = models.FloatField('Capacidad de campo')
    wilting_point = models.FloatField('Punto de marchitez')
    permeability= models.FloatField('Permiabilidad')
    porosity= models.FloatField('Porosidad')
    
    class Meta:
        db_table = 'Drenaje_suelo'
        verbose_name_plural='Drenajes del suelo'




