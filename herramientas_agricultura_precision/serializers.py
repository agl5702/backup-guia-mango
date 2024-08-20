from rest_framework import serializers
from herramientas_agricultura_precision.models import Herramientas


# Serializer Views
class HerramientasSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Herramientas
        fields ='__all__'
        
