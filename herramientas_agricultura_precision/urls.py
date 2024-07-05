from django.urls import path,include
from herramientas_agricultura_precision.serializers import HerramientasSerializer,TipoMercadoSerializer
from herramientas_agricultura_precision.views import HerramientasView,TipoMercadoView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'hdap',HerramientasView, 'Herramientas de agricultura de precisión')
router.register(r'tipo-mercado',TipoMercadoView, 'Tipo de mercado')


urlpatterns = [
    path('',include(router.urls)),
]
