from rest_framework import serializers
from variedad_mango.models import VariedadMango

class VariedadMangoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VariedadMango
        fields = '__all__'
