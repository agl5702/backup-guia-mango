from django.urls import path,include
from nutrientes.views import NutrientesView,pHView,TipoTerrenoView,TipoSueloView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'nutrientes',NutrientesView, 'nutrientes')
router.register(r'ph',pHView, 'ph')
router.register(r'tipo-terreno',TipoTerrenoView, 'tipo de terreno')
router.register(r'tipo-suelo',TipoSueloView, 'tipo de suelo')


urlpatterns = [
    path('',include(router.urls)),
]
