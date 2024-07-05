from rest_framework import viewsets
from cultivo.models import Cultivo
from cultivo.serializers import CultivoSerializer
# Create your views here.

class CultivoView(viewsets.ModelViewSet):
    
    serializer_class = CultivoSerializer
    queryset = Cultivo.objects.all()