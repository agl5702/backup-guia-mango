from rest_framework import viewsets
from variedad_mango.models import VariedadMango
from variedad_mango.serializers import VariedadMangoSerializer
from drf_yasg.utils import swagger_auto_schema # type: ignore
from drf_yasg import openapi # type: ignore


# Create your views here.

class VariedadMangoView(viewsets.ModelViewSet):
    
    serializer_class = VariedadMangoSerializer
    queryset = VariedadMango.objects.all()

    @swagger_auto_schema(
        operation_description="Obtener todas las variedades de mango",
        responses={200: VariedadMangoSerializer()},
        operation_summary="Lista de todas las variedades de mango",
        tags= ['Variedades de Mango']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtener la variedad de mango por ID",
        responses={200: VariedadMangoSerializer()},
        operation_summary="Obtener variedad de mango por ID",
        tags= ['Variedades de Mango']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Crear una variedad de mango",
        responses={200: VariedadMangoSerializer()},
        operation_summary="Crea una variedad de mango",
        tags= ['Variedades de Mango']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualizar una variedad de mango",
        responses={200: VariedadMangoSerializer},
        operation_summary="Actualizar una variedad de mango",
        tags= ['Variedades de Mango']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualizar parcialmente una variedad de mango",
        responses={200: VariedadMangoSerializer()},
        operation_summary="Actualizar parcialmente una variedad de mango",
        tags=['Variedades de Mango']
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


    @swagger_auto_schema(
        operation_description="Eliminar una variedad de mango",
        responses={200: VariedadMangoSerializer()},
        operation_summary="Eliminar una variedad de mango",
        tags= ['Variedades de Mango']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

