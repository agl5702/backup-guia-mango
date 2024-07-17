from django.urls import path,include
from variedad_mango.views import VariedadMangoView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'variedad-mango',VariedadMangoView, 'Variedad de mango')



urlpatterns = [
    path('',include(router.urls)),
]
