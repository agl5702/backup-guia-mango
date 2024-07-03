from django.urls import path,include
from tipo_siembra.views import TipoSiembraView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tipo-siembra',TipoSiembraView, 'tipo de siembra')


urlpatterns = [
    path('',include(router.urls)),
]
