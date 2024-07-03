from rest_framework import viewsets
from nutrientes.models import Nutrientes,pH,TipoTerreno,TipoSuelo
from nutrientes.serializers import NutrientesSerializer,pHSerializer,TipoTerrenoSerializer,TipoSueloSerializer


# Create your views here.
class NutrientesView(viewsets.ModelViewSet):
    
    serializer_class = NutrientesSerializer
    queryset = Nutrientes.objects.all()
    
class pHView(viewsets.ModelViewSet):
    serializer_class = pHSerializer
    queryset = pH.objects.all()
    
class TipoTerrenoView(viewsets.ModelViewSet):
    serializer_class = TipoTerrenoSerializer
    queryset = TipoTerreno.objects.all()

class TipoSueloView(viewsets.ModelViewSet):
    serializer_class= TipoSueloSerializer
    queryset = TipoSuelo.objects.all()