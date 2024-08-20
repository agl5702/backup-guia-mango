from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema # type: ignore
from drf_yasg import openapi # type: ignore

from herramientas_agricultura_precision.models import Herramientas
from herramientas_agricultura_precision.serializers import HerramientasSerializer

# Create your views here.
class HerramientasView(viewsets.ModelViewSet):
    
    serializer_class =HerramientasSerializer
    queryset= Herramientas.objects.all()
    
    @swagger_auto_schema(
        operation_description="Obtener todas las herramientas de agricultura de precisión",
        responses={200: HerramientasSerializer()},
        operation_summary="Lista de todas las herramientas",
        tags= ['Herramientas']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtener la herramienta por ID",
        responses={200: HerramientasSerializer()},
        operation_summary="Obtener herramientas por ID",
        tags= ['Herramientas']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Crear herramienta",
        responses={200: HerramientasSerializer()},
        operation_summary="Crea una nueva herramienta",
        tags= ['Herramientas']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualizar herramienta",
        responses={200: HerramientasSerializer()},
        operation_summary="Actualizar una herramienta existente",
        tags= ['Herramientas']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualizar parcialmente una herramienta.",
        responses={200: HerramientasSerializer()},
        operation_summary="Actualizar parcialmente una herramienta",
        tags=['Herramientas']
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    

    @swagger_auto_schema(
        operation_description="Eliminar herramienta",
        responses={200: HerramientasSerializer()},
        operation_summary="Eliminar una herramienta existente",
        tags= ['Herramientas']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


