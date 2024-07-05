from django.urls import path,include
from analisis_foliar.views import AnalisisFoliarView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'analisis-foliar',AnalisisFoliarView, 'analisis-foliar')

urlpatterns = [
    path('',include(router.urls)),
]
