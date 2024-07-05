from django.urls import path,include
from variedad_mango.views import VariedadMangoView,AnalisisSueloView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'variedad-mango',VariedadMangoView, 'Variedad de mango')
router.register(r'analisis-suelo',AnalisisSueloView, 'analisis del suelo')



urlpatterns = [
    path('',include(router.urls)),
]
