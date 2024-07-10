from rest_framework import viewsets
from hectareas.serializers import HectareasSerializer
from hectareas.models import Hectareas
from drf_yasg.utils import swagger_auto_schema # type: ignore
from drf_yasg import openapi # type: ignore

# Create your views here.
class HectareasView(viewsets.ModelViewSet):
    
    serializer_class =HectareasSerializer
    queryset = Hectareas.objects.all()

    @swagger_auto_schema(
        operation_description="Obtener todas las hectáreas",
        responses={200: HectareasSerializer()},
        operation_summary="Lista de todas las hectáreas",
        tags= ['Hectáreas']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtener la hectáreas por ID",
        responses={200: HectareasSerializer()},
        operation_summary="Obtener hectáreas por ID",
        tags= ['Hectáreas']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Crear medidas de hectáreas",
        responses={200: HectareasSerializer()},
        operation_summary="Crea una nueva medida de hectáreas",
        tags= ['Hectáreas']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualizar una medida de hectárea",
        responses={200: HectareasSerializer},
        operation_summary="Actualizar una medida de hectárea",
        tags= ['Hectáreas']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualizar parcialmente una medida de hectárea",
        responses={200: HectareasSerializer()},
        operation_summary="Actualizar parcialmente una medida de hectárea",
        tags=['Hectáreas']
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


    @swagger_auto_schema(
        operation_description="Eliminar una medida de hectárea",
        responses={200: HectareasSerializer()},
        operation_summary="Eliminar una medida de hectárea",
        tags= ['Hectáreas']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)