from rest_framework import viewsets
from suelo.models import FertilidadSuelo,pH,TipoTerreno,TipoSuelo
from suelo.serializers import FertilidadSueloSerializer,pHSerializer,TipoTerrenoSerializer,TipoSueloSerializer


# Create your views here.
class FertilidadSueloView(viewsets.ModelViewSet):
    """
    crear, eliminar, actualizar, nutrientes
    """
    serializer_class = FertilidadSueloSerializer
    queryset = FertilidadSuelo.objects.all()


    
class pHView(viewsets.ModelViewSet):
    """
    crear, eliminar, actualizar, ph
    """
    serializer_class = pHSerializer
    queryset = pH.objects.all()
    
class TipoTerrenoView(viewsets.ModelViewSet):
    """
    crear, eliminar, actualizar, tipos de terrenos
    """
    serializer_class = TipoTerrenoSerializer
    queryset = TipoTerreno.objects.all()

class TipoSueloView(viewsets.ModelViewSet):
    """
    crear, eliminar, actualizar, tipos de suelo 
    """
    serializer_class= TipoSueloSerializer
    queryset = TipoSuelo.objects.all()