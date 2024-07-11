from django.db import models

# Modelos
class FertilidadSuelo(models.Model):
    level_choices = [
        ('BAJO','Bajo'),
        ('OPTIMO','Optimo'),
        ('ELEVADO','Elevado'),
        ]

    name = models.CharField('Nombre del nutriente',max_length=45)
    description = models.CharField('Descripción del nutriente',max_length=500)
    level = models.CharField('Nivel del nutiente', choices=level_choices,max_length=255,default='OPTIMO')
    value =models.FloatField('Valor del nutriente')

    class Meta:
        db_table='Fertilidad_suelo'
        verbose_name_plural = 'FertilidadSuelo'
    def __str__(self):
        return self.name
# Ph    
class pH(models.Model):
    level_choices = [
        ('BAJO','Bajo'),
        ('OPTIMO','Optimo'),
        ('ELEVADO','Elevado'),
    ]


    description = models.CharField(max_length=500)
    value = models.FloatField('Valor del pH',default=7.0, null=False, blank=False)
    level = models.CharField('Nivel del nutiente', choices=level_choices,max_length=255,default='OPTIMO')

    class Meta:
        db_table = 'ph'
        verbose_name_plural = 'pH'

    def __str__(self):
        return self.value
    
#Tipo de Terreno   
class TipoTerreno(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=500)

    class Meta:
        db_table = 'Tipo_terreno'
        verbose_name_plural = 'Tipos de terrenos'

    def __str__(self):
        return self.name
    
# Tipos de suelo 
class TipoSuelo(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=500)
    # change 
    nutrients = models.ManyToManyField(FertilidadSuelo)
    ph = models.ForeignKey(pH, on_delete=models.CASCADE)
    type_of_terrain = models.ForeignKey(TipoTerreno, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tipo_suelo'
        verbose_name_plural = 'Tipos de suelos'

    def __str__(self):
        return self.name
    
#Textura de suelo
class TexturaSuelo(models.Model):
    name_choices= [
        ('Arena', 'Arena'),
        ('Limo', 'Limo'),
        ('Arcilla', 'Arcilla'),
    ]
    name = models.CharField('Nombre de textura',max_length=20, choices=name_choices,default='')
    value = models.FloatField()
    description = models.TextField('Descripción')

    class Meta:
        db_table = 'Textura_Suelo'
        verbose_name_plural = 'Texturas del suelo'

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




