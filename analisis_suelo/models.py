from django.db import models
from django.conf import settings
from suelo.models import TipoSuelo,TexturaSuelo
from django.contrib.auth import get_user_model  
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Modelo de usuario
UserModel = get_user_model()



class AnalisisSuelo(models.Model):
    name = models.CharField(max_length=20,editable=False,default='Análisis del suelo')
    infiltration_rate = models.FloatField()
    field_capacity = models.FloatField()
    point_wither = models.FloatField()
    permeability = models.FloatField()
    porosity = models.FloatField()
    alert= models.BooleanField('Alerta',default=False)
    message = models.CharField(max_length=1000,blank=False,null=False)
    description = models.CharField(max_length=1000)
    ph = models.FloatField(null=False)
    nitrogen = models.FloatField(null=False)
    phosphorus = models.FloatField(null=False)
    potassium = models.FloatField(null=False)
    calcium = models.FloatField(null=False)
    magnesium = models.FloatField(null=False)
    sulfur = models.FloatField(null=False)
    iron = models.FloatField(null=False)
    manganese = models.FloatField(null=False)
    zinc = models.FloatField(null=False)
    copper = models.FloatField(null=False)
    molybdenum = models.FloatField(null=False)
    boron = models.FloatField(null=False)
    soil_type = models.ForeignKey(TipoSuelo, on_delete=models.CASCADE)
    soil_texture=models.ForeignKey(TexturaSuelo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(UserModel, on_delete=models.CASCADE,default=get_user_model())    # usuario --- añadir
    
    class Meta:
        verbose_name_plural = 'Analisis del suelo'
        db_table = 'analisis_de_suelo'
    
    
    def save(self, *args, **kwargs):
        # Si el usuario no está establecido y la instancia no ha sido guardada previamente
        if not self.usuario_id and not self.pk:
            # Establecer el usuario actual como el creador del torneo
            self.usuario = self._get_default_user()
        super().save(*args, **kwargs)

    def _get_default_user(self):
        # Obtener el usuario actual o el usuario predeterminado (si no hay uno autenticado)
        return getattr(self, 'usuario', None) or UserModel.objects.get(pk=settings.DEFAULT_USER_ID)
    
    def __str__(self):
        return self.name
