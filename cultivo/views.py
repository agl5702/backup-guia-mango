from rest_framework import viewsets
from cultivo.models import Cultivo
from cultivo.serializers import CultivoSerializer
from drf_yasg.utils import swagger_auto_schema # type: ignore
from drf_yasg import openapi # type: ignore
# Create your views here.

class CultivoView(viewsets.ModelViewSet):
    
    serializer_class = CultivoSerializer
    queryset = Cultivo.objects.all()

    @swagger_auto_schema(
        operation_description="Obtener todos los cultivos",
        responses={200: CultivoSerializer(many=True)},
        operation_summary="Obten una Lista de los cultivos",
        tags= ['Cultivos']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtener un cultivo por su ID.",
        responses={200: CultivoSerializer()},
        operation_summary="Obeter cultivo por ID",
        tags= ['Cultivos']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Crear un nuevo cultivo",
        responses={200: CultivoSerializer()},
        operation_summary="Crea un cultivo",
        tags= ['Cultivos']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualizar cultivo por ID",
        responses={200: CultivoSerializer()},
        operation_summary="Actualiza un cultivo por ID",
        tags= ['Cultivos']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Actualizar parcialmente un cultivo",
        responses={200: CultivoSerializer()},
        operation_summary="Actualizar parcialmente un cultivo",
        tags=['Cultivos']
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Eliminar un cultivo por ID.",
        responses={204: "No content"},
        operation_summary="Elimina un cultivo por ID",
        tags= ['Cultivos']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)