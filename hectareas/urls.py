from django.urls import path,include
from hectareas.serializers import HectareasSerializer
from hectareas.views import HectareasView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'hectareas',HectareasView, 'Hectáreas')


urlpatterns = [
    path('',include(router.urls)),
]
