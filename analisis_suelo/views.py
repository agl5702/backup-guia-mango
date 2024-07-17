from rest_framework import viewsets
from analisis_suelo.models import AnalisisSuelo
from analisis_suelo.serializers import AnalisisSueloSerializer
from drf_yasg.utils import swagger_auto_schema # type: ignore
from drf_yasg import openapi # type: ignore



class AnalisisSueloView(viewsets.ModelViewSet):
    
    serializer_class = AnalisisSueloSerializer
    queryset = AnalisisSuelo.objects.all()

    @swagger_auto_schema(
        operation_description="Obtener todos los análisis del suelo",
        responses={200: AnalisisSueloSerializer(many=True)},
        operation_summary="Obten una Lista de los análisis del suelo",
        tags= ['Análisis del Suelo']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtener un análisis del suelo por su ID.",
        responses={200: AnalisisSueloSerializer()},
        operation_summary="Obeter un análisis del suelo por ID",
        tags= ['Análisis del Suelo']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Crear un análisis del suelo",
        responses={200: AnalisisSueloSerializer()},
        operation_summary="Crea un análisis del suelo",
        tags= ['Análisis del Suelo']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualizar análisis del suelo por ID",
        responses={200: AnalisisSueloSerializer()},
        operation_summary="Actualiza un análisis del suelo por ID",
        tags= ['Análisis del Suelo']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Actualizar parcialmente un análisis del suelo",
        responses={200: AnalisisSueloSerializer()},
        operation_summary="Actualizar parcialmente un análisis del suelo",
        tags=['Análisis del Suelo']
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Eliminar un análisis del suelo por ID.",
        responses={204: "No content"},
        operation_summary="Elimina un análisis del suelo por ID",
        tags= ['Análisis del Suelo']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)