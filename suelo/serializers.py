from rest_framework import serializers
from suelo.models import FertilidadSuelo,pH,TipoSuelo


class FertilidadSueloSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FertilidadSuelo
        fields = '__all__'
        
class pHSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = pH
        fields = '__all__'


class TipoSueloSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TipoSuelo
        fields = '__all__'