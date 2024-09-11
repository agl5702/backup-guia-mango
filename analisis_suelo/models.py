from django.db import models
from django.conf import settings
from suelo.models import TipoSuelo, TexturaSuelo
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Modelo de usuario
UserModel = get_user_model()

class AnalisisSuelo(models.Model):
    name = models.CharField(max_length=20, editable=False, default='Análisis del suelo')
    message = models.CharField(max_length=1000, blank=False,editable=False, null=False, default="")
    description = models.CharField(max_length=1000,default="",editable=False)
    
    # Texture 
    sand = models.FloatField(null=False)
    silt = models.FloatField(null=False)
    clay = models.FloatField(null=False)    
    
    # pH
    ph = models.FloatField(null=False)
    
    # Nutrients
    nh4 = models.FloatField(null=False)
    nh3 = models.FloatField(null=False)
    phosphorus = models.FloatField(null=False)
    potassium = models.FloatField(null=False)
    calcium = models.FloatField(null=False)
    magnesium = models.FloatField(null=False)
    sodium = models.FloatField(null=False)
    aluminum = models.FloatField(null=False)
    sulfur = models.FloatField(null=False)
    iron = models.FloatField(null=False)
    manganese = models.FloatField(null=False)
    zinc = models.FloatField(null=False)
    copper = models.FloatField(null=False)
    boron = models.FloatField(null=False)
    
    # Fields for density and depth
    densidad_aparente = models.FloatField(null=False)  # g/cm³
    profundidad_cm = models.FloatField(null=False)  # cm
    
    # Calculate soil texture
    soil_texture = models.ForeignKey(TipoSuelo, on_delete=models.CASCADE,editable=False, null=True, blank=True)
    
    # User 
    usuario = models.ForeignKey(UserModel, on_delete=models.CASCADE, default=get_user_model())
    
    # Campos para almacenar los valores en kg/ha
    potassium_kg_per_ha = models.FloatField(null=True, blank=True,editable=False,default=0)
    calcium_kg_per_ha = models.FloatField(null=True, blank=True,editable=False,default=0)
    magnesium_kg_per_ha = models.FloatField(null=True, blank=True,editable=False,default=0)
    sodium_kg_per_ha = models.FloatField(null=True, blank=True,editable=False,default=0)
    phosphorus_kg_per_ha = models.FloatField(null=True, blank=True,editable=False,default=0)
    nh4_kg_per_ha = models.FloatField(null=True, blank=True,editable=False,default=0)
    nh3_kg_per_ha = models.FloatField(null=True, blank=True,editable=False,default=0)
    sulfur_kg_per_ha = models.FloatField(null=True, blank=True,editable=False,default=0)
    iron_kg_per_ha = models.FloatField(null=True, blank=True,editable=False,default=0)
    manganese_kg_per_ha = models.FloatField(null=True, blank=True,editable=False,default=0)
    copper_kg_per_ha = models.FloatField(null=True, blank=True,editable=False,default=0)
    zinc_kg_per_ha = models.FloatField(null=True, blank=True,editable=False,default=0)
    boron_kg_per_ha = models.FloatField(null=True, blank=True,editable=False,default=0)
    
    class Meta:
        verbose_name_plural = 'Analisis del suelo'
        db_table = 'analisis_de_suelo'
    

    def get_context_data(self, **kwargs):
        # Llama al método de la clase base para obtener el contexto inicial
        context = super().get_context_data(**kwargs)
        
        # Obtén el usuario autenticado
        user = self.request.user

        # Filtrar los torneos para que solo incluyan aquellos asociados con el usuario autenticado
        analisis = AnalisisSuelo.objects.filter(usuario=user)

        # Agrega los torneos filtrados al contexto
        context['analisis'] = analisis
    
        return context

    def save(self, *args, **kwargs):
        # Si el usuario no está establecido y la instancia no ha sido guardada previamente
        if not self.usuario_id and not self.pk:
            self.usuario = self._get_default_user() or  UserModel.objects.first()
        
        # Convertir meq/100cc a mg/kg
        self.potassium = round(self.convert_to_mg_per_kg(self.potassium, 39.098, 1), 2)
        self.calcium = round(self.convert_to_mg_per_kg(self.calcium, 40.078, 2), 2)
        self.magnesium = round(self.convert_to_mg_per_kg(self.magnesium, 24.305, 2), 2)
        self.sodium = round(self.convert_to_mg_per_kg(self.sodium, 22.989769, 1), 2)
        
        # Calcular kg/ha
        self.potassium_kg_per_ha = round(self.calculate_kg_per_ha(self.potassium), 2)
        self.calcium_kg_per_ha = round(self.calculate_kg_per_ha(self.calcium), 2)
        self.magnesium_kg_per_ha = round(self.calculate_kg_per_ha(self.magnesium), 2)
        self.sodium_kg_per_ha = round(self.calculate_kg_per_ha(self.sodium), 2)
        self.phosphorus_kg_per_ha = round(self.calculate_kg_per_ha(self.phosphorus), 2)
        self.nh4_kg_per_ha = round(self.calculate_kg_per_ha(self.nh4), 2)
        self.nh3_kg_per_ha = round(self.calculate_kg_per_ha(self.nh3), 2)
        self.sulfur_kg_per_ha = round(self.calculate_kg_per_ha(self.sulfur), 2)
        self.iron_kg_per_ha = round(self.calculate_kg_per_ha(self.iron), 2)
        self.manganese_kg_per_ha = round(self.calculate_kg_per_ha(self.manganese), 2)
        self.copper_kg_per_ha = round(self.calculate_kg_per_ha(self.copper), 2)
        self.zinc_kg_per_ha = round(self.calculate_kg_per_ha(self.zinc), 2)
        self.boron_kg_per_ha = round(self.calculate_kg_per_ha(self.boron), 2)

        self.soil_texture = self.get_soil_type()

        super().save(*args, **kwargs)

    def _get_default_user(self):
        if self.usuario:
            return self.usuario

        # Si no hay usuario, intentar obtener uno predeterminado (por ejemplo, el primer usuario en la base de datos)
        try:
            return UserModel.objects.first()  # O puedes usar alguna lógica personalizada para obtener un usuario predeterminado
        except UserModel.DoesNotExist:
            # Crear un usuario predeterminado si no existe
            default_user = UserModel.objects.create(username="default_user", email="default@example.com")
            return default_user   
    def get_soil_type(self):
        """
        Determina el tipo de suelo basado en los porcentajes de arena, limo y arcilla.
        """
        tipos_suelo = TipoSuelo.objects.all()
        for tipo in tipos_suelo:
            if (tipo.sand_min <= self.sand <= tipo.sand_max and
                tipo.silt_min <= self.silt <= tipo.silt_max and
                tipo.clay_min <= self.clay <= tipo.clay_max):
                return tipo
        return None  # O puedes lanzar una excepción si no se encuentra un tipo de suelo adecuado

    def convert_to_mg_per_kg(self, value_meq, atomic_weight, valence):
        """
        Convierte el valor de meq/100cc a mg/kg
        """
        return (value_meq * atomic_weight) / valence

    def calculate_kg_per_ha(self, value_ppm):
        """
        Calcula el valor en kg/ha usando la fórmula: valor_ppm * densidad_aparente * profundidad_cm * 10 / 100
        """
        return (value_ppm * self.densidad_aparente * self.profundidad_cm * 10) / 100




    
    
    def __str__(self):
        return f" Análisis n° {self.id}"
