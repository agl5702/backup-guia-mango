from rest_framework import serializers
from herramientas_agricultura_precision.models import HerAgri,TipoMercado


# Serializer Views
class HerAgriSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HerAgri
        fields ='__all__'
        
class TipoMercadoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TipoMercado
        fields= '__all__'