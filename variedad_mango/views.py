from rest_framework import viewsets
from variedad_mango.models import VariedadMango,AnalisisSuelo
from variedad_mango.serializers import VariedadMangoSerializer,AnalisisSueloSerializer
# Create your views here.

class VariedadMangoView(viewsets.ModelViewSet):
    
    serializer_class = VariedadMangoSerializer
    queryset = VariedadMango.objects.all()

class AnalisisSueloView(viewsets.ModelViewSet):
    
    serializer_class = AnalisisSueloSerializer
    queryset = AnalisisSuelo.objects.all()