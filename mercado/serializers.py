from rest_framework import serializers
from mercado.models import TipoMercado

class TipoMercadoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TipoMercado
        fields= '__all__'