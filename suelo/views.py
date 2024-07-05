from rest_framework import viewsets
from suelo.models import FertilidadSuelo,pH,TipoTerreno,TipoSuelo
from suelo.serializers import FertilidadSueloSerializer,pHSerializer,TipoTerrenoSerializer,TipoSueloSerializer


# Create your views here.
class FertilidadSueloView(viewsets.ModelViewSet):
    
    serializer_class = FertilidadSueloSerializer
    queryset = FertilidadSuelo.objects.all()


    
class pHView(viewsets.ModelViewSet):
    serializer_class = pHSerializer
    queryset = pH.objects.all()
    
class TipoTerrenoView(viewsets.ModelViewSet):
    serializer_class = TipoTerrenoSerializer
    queryset = TipoTerreno.objects.all()

class TipoSueloView(viewsets.ModelViewSet):
    serializer_class= TipoSueloSerializer
    queryset = TipoSuelo.objects.all()