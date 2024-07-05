from rest_framework import serializers
from variedad_mango.models import VariedadMango,AnalisisSuelo


class VariedadMangoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VariedadMango
        fields = '__all__'
        
class AnalisisSueloSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AnalisisSuelo
        fields= '__all__'

