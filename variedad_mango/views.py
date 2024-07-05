from rest_framework import viewsets
from variedad_mango.models import VariedadMango,AptitudSuelo
from variedad_mango.serializers import VariedadMangoSerializer,AptitudSueloSerializer
# Create your views here.

class VariedadMangoView(viewsets.ModelViewSet):
    
    serializer_class = VariedadMangoSerializer
    queryset = VariedadMango.objects.all()

class AptitudSueloView(viewsets.ModelViewSet):
    
    serializer_class = AptitudSueloSerializer
    queryset = AptitudSuelo.objects.all()