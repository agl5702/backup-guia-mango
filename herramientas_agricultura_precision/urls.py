from django.urls import path,include
from herramientas_agricultura_precision.views import HerramientasView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'hdap',HerramientasView, 'Herramientas de agricultura de precisión')


urlpatterns = [
    path('',include(router.urls)),
]
