from rest_framework import viewsets
from tipo_siembra.models import TipoSiembra
from tipo_siembra.serializers import TipoSiembraSerializer
# Create your views here.
class TipoSiembraView(viewsets.ModelViewSet):
    serializer_class =TipoSiembraSerializer
    queryset= TipoSiembra.objects.all()
