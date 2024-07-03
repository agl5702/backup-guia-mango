from rest_framework import viewsets
from hectareas.serializers import HectareasSerializer
from hectareas.models import Hectareas

# Create your views here.
class HectareasView(viewsets.ModelViewSet):
    
    serializer_class =HectareasSerializer
    queryset = Hectareas.objects.all()