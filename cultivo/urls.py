from django.urls import path,include
from cultivo.views import CultivoView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cultivos',CultivoView, 'Cultivos')

urlpatterns = [
    path('',include(router.urls)),
]
