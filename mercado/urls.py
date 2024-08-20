from django.urls import path,include
from mercado.serializers import TipoMercadoSerializer
from mercado.views import TipoMercadoView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tipo-mercado',TipoMercadoView, 'Tipo de mercado')


urlpatterns = [
    path('',include(router.urls)),
]
