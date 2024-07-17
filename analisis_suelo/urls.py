from django.urls import path,include
from analisis_suelo.views import AnalisisSueloView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'analisis-suelo',AnalisisSueloView, 'analisis-del-suelo')

urlpatterns = [
    path('',include(router.urls)),
]
