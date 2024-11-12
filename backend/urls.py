
from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Tu API",
        default_version='v1',
        description="Descripción de tu API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@tuapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
schema_view.security = [{'Bearer': []}] 

from users.views import Login,Logout
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('usuario/', include('users.api.urls')),
    path('login/',Login.as_view(), name='login'),
    path('logout/',Logout.as_view(), name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tipo-de-siembra/',include('tipo_siembra.urls')),
    path('mercado/',include('mercado.urls')),
    path('herramientas-de-agricultura-de-presicion/',include('herramientas_agricultura_precision.urls')),
    path('hectareas/',include('hectareas.urls')),
    path('suelo/',include('suelo.urls')),
    path('analisis-suelo/',include('analisis_suelo.urls')),
    path('variedad-mango/',include('variedad_mango.urls')),
    path('cultivo/',include('cultivo.urls')),    
    path('analisis-foliar/',include('analisis_foliar.urls')),    
    path('plagas/',include('plagas.urls')),    

]
