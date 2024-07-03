from rest_framework import serializers
from tipo_siembra.models import TipoSiembra


# Serializers Class
class TipoSiembraSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= TipoSiembra
        fields = '__all__'
            
    