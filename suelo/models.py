from django.db import models

# Modelos
class FertilidadSuelo(models.Model):
    level_choices = [
        ('BAJO','Bajo'),
        ('OPTIMO','Optimo'),
        ('ELEVADO','Elevado'),
        ]

    name = models.CharField('Nombre del nutriente',max_length=45)
    description = models.TextField('Descripción del nutriente',max_length=500)
    level = models.CharField('Nivel del nutiente', choices=level_choices,max_length=255,default='OPTIMO')
    min_value =models.FloatField('Valor mínimo del nutriente')
    max_value =models.FloatField('Valor máximo nutriente')

    class Meta:
        db_table='Fertilidad_suelo'
        verbose_name_plural = 'FertilidadSuelo'
    def __str__(self):
        return self.name
# Ph    
class pH(models.Model):
    level_choices = [
        ('Bajo','Bajo'),
        ('Optimo','Optimo'),
        ('Elevado','Elevado'),
    ]


    description = models.TextField(max_length=500)
    min_value = models.FloatField('Valor mínimo del pH',default=5.5, null=False, blank=False)
    max_value = models.FloatField('Valor máximo del pH',default=7.0, null=False, blank=False)
    level = models.CharField('Nivel del nutiente', choices=level_choices,max_length=255,default='Optimo')

    class Meta:
        db_table = 'ph'
        verbose_name_plural = 'pH'

    def __str__(self):
        return f" Ph - {self.level}"
class Conductividad(models.Model):
    level_choices = [
        ('Bajo','Bajo'),
        ('Optimo','Optimo'),
        ('Elevado','Elevado'),
    ]

    description = models.TextField(max_length=500)
    level = models.CharField('Nivel del nutiente', choices=level_choices,max_length=255,default='Optimo')
    value=models.FloatField(null=False)
    
#Textura de suelo
class TexturaSuelo(models.Model):

    name = models.CharField('Nombre de textura',max_length=20)
    description = models.TextField('Descripción')
    class Meta:
        db_table = 'Textura_Suelo'
        verbose_name_plural = 'Texturas del suelo'

    def __str__(self):
        return self.name

    
# Tipos de suelo 
class TipoSuelo(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=500)
    # change 
    ph = models.ForeignKey(pH, on_delete=models.CASCADE)

    sand_min = models.FloatField(null=False, help_text="Porcentaje mínimo de arena")
    sand_max = models.FloatField(null=False, help_text="Porcentaje máximo de arena")
    
    silt_min = models.FloatField(null=False, help_text="Porcentaje mínimo de limo")
    silt_max = models.FloatField(null=False, help_text="Porcentaje máximo de limo")
    
    clay_min = models.FloatField(null=False, help_text="Porcentaje mínimo de arcilla")
    clay_max = models.FloatField(null=False, help_text="Porcentaje máximo de arcilla")
    class Meta:
        db_table = 'tipo_suelo'
        verbose_name_plural = 'Tipos de suelos'

    def __str__(self):
        return self.name
    

# Drenaje del suelo
class DrenajeSuelo(models.Model):
    # Eliminar choices
   
    # Eliminar campo level
    value = models.FloatField('Valor de referencia')
    infiltration_rate= models.FloatField('Tasa de infiltración')
    field_capacity = models.FloatField('Capacidad de campo')
    wilting_point = models.FloatField('Punto de marchitez')
    permeability= models.FloatField('Permiabilidad')
    porosity= models.FloatField('Porosidad')
    
    class Meta:
        db_table = 'Drenaje_suelo'
        verbose_name_plural='Drenajes del suelo'




