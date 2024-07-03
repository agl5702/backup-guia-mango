from rest_framework import serializers
from hectareas.models import Hectareas


class HectareasSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hectareas
        fields ='__all__'