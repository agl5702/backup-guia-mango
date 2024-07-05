from rest_framework import serializers
from variedad_mango.models import VariedadMango,AptitudSuelo


class VariedadMangoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VariedadMango
        fields = '__all__'
        
class AptitudSueloSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AptitudSuelo
        fields= '__all__'

