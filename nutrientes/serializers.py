from rest_framework import serializers
from nutrientes.models import Nutrientes,pH,TipoTerreno,TipoSuelo


class NutrientesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Nutrientes
        fields = '__all__'
        
class pHSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = pH
        fields = '__all__'

class TipoTerrenoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TipoTerreno
        fields = '__all__'
class TipoSueloSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TipoSuelo
        fields = '__all__'