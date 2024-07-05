from rest_framework import serializers
from herramientas_agricultura_precision.models import Herramientas,TipoMercado


# Serializer Views
class HerramientasSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Herramientas
        fields ='__all__'
        
class TipoMercadoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TipoMercado
        fields= '__all__'