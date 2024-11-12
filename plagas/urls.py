from django.urls import path,include
from plagas.views import PlagaView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'plagas', PlagaView,'plagas')

urlpatterns = [
    path('', include(router.urls)),
]
