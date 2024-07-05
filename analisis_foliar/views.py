from rest_framework import viewsets
from analisis_foliar.models import AnalisisFoliar
from analisis_foliar.serializers import AnalisisFoliarSerializer

# Create your views here.
class AnalisisFoliarView(viewsets.ModelViewSet):
    
    serializer_class = AnalisisFoliarSerializer
    queryset = AnalisisFoliar.objects.all()