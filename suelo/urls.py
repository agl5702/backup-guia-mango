from django.urls import path,include
from suelo.views import FertilidadSueloView,pHView,TipoTerrenoView,TipoSueloView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'suelo',FertilidadSueloView, 'suelo')
router.register(r'ph',pHView, 'ph')
router.register(r'tipo-terreno',TipoTerrenoView, 'tipo de terreno')
router.register(r'tipo-suelo',TipoSueloView, 'tipo de suelo')


urlpatterns = [
    path('',include(router.urls)),
]
