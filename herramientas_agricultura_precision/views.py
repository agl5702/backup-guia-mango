from rest_framework import viewsets
from herramientas_agricultura_precision.models import HerAgri,TipoMercado
from herramientas_agricultura_precision.serializers import HerAgriSerializer,TipoMercadoSerializer

# Create your views here.
class HerAgriView(viewsets.ModelViewSet):
    
    serializer_class =HerAgriSerializer
    queryset= HerAgri.objects.all()
    
class TipoMercadoView(viewsets.ModelViewSet):
    
    serializer_class=TipoMercadoSerializer
    queryset= TipoMercado.objects.all()
