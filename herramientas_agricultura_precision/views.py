from rest_framework import viewsets
from herramientas_agricultura_precision.models import Herramientas,TipoMercado
from herramientas_agricultura_precision.serializers import HerramientasSerializer,TipoMercadoSerializer

# Create your views here.
class HerramientasView(viewsets.ModelViewSet):
    
    serializer_class =HerramientasSerializer
    queryset= Herramientas.objects.all()
    
class TipoMercadoView(viewsets.ModelViewSet):
    
    serializer_class=TipoMercadoSerializer
    queryset= TipoMercado.objects.all()
