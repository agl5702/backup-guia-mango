from rest_framework import serializers
from analisis_foliar.models import AnalisisFoliar

class AnalisisFoliarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AnalisisFoliar
        fields= '__all__'
