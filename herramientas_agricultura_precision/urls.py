from django.urls import path,include
from herramientas_agricultura_precision.serializers import HerAgriSerializer,TipoMercadoSerializer
from herramientas_agricultura_precision.views import HerAgriView,TipoMercadoView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'hdap',HerAgriView, 'Herramientas de agricultura de precisión')
router.register(r'tipo-mercado',TipoMercadoView, 'Tipo de mercado')


urlpatterns = [
    path('',include(router.urls)),
]
