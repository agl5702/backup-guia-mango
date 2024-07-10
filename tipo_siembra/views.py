from rest_framework import viewsets 
from drf_yasg.utils import swagger_auto_schema 
from drf_yasg import openapi
from tipo_siembra.models import TipoSiembra
from tipo_siembra.serializers import TipoSiembraSerializer

class TipoSiembraView(viewsets.ModelViewSet):
    serializer_class = TipoSiembraSerializer
    queryset = TipoSiembra.objects.all()

    @swagger_auto_schema(
        operation_description="Obtener todos los tipos de siembra.",
        responses={200: TipoSiembraSerializer(many=True)},
        operation_summary="Lista de tipos de siembra",
        tags= ['Siembra']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtener un tipo de siembra por su ID.",
        responses={200: TipoSiembraSerializer()},
        operation_summary="Obeter tipo de siembra por ID",
        tags= ['Siembra']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Crear un nuevo tipo de siembra.",
        responses={200: TipoSiembraSerializer()},
        operation_summary="Crea un tipo de siembra",
        tags= ['Siembra']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualizar un tipo de siembra existente.",
        responses={200: TipoSiembraSerializer()},
        operation_summary="Actualiza un tipo de siembra",
        tags= ['Siembra']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Actualizar parcialmente un tipo de siembra existente.",
        responses={200: TipoSiembraSerializer()},
        operation_summary="Actualizar parcialmente un tipo de siembra",
        tags=['Siembra']
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Eliminar un tipo de siembra existente.",
        responses={204: "No content"},
        operation_summary="Elimina un tipo de siembra por ID",
        tags= ['Siembra']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
