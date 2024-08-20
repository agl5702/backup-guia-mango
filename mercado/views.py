from django.shortcuts import render
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema # type: ignore
from drf_yasg import openapi # type: ignore

from mercado.models import TipoMercado
from mercado.serializers import TipoMercadoSerializer
# Create your views here.
class TipoMercadoView(viewsets.ModelViewSet):
    
    serializer_class=TipoMercadoSerializer
    queryset= TipoMercado.objects.all()

    @swagger_auto_schema(
        operation_description="Obtener todas las herramientas de agricultura de precisión",
        responses={200: TipoMercadoSerializer()},
        operation_summary="Lista de todas las herramientas",
        tags= ['Tipo de Mercados']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtener la herramienta por ID",
        responses={200: TipoMercadoSerializer()},
        operation_summary="Obtener herramientas por ID",
        tags= ['Tipo de Mercados']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Crear un tipo de mercado",
        responses={200: TipoMercadoSerializer()},
        operation_summary="Crea una nuevo tipo de mercado",
        tags= ['Tipo de Mercados']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualizar un tipo de mercado",
        responses={200: TipoMercadoSerializer()},
        operation_summary="Actualizar un tipo de mercado existente",
        tags= ['Tipo de Mercados']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualizar parcialmente un tipo de mercado.",
        responses={200: TipoMercadoSerializer()},
        operation_summary="Actualizar tipo de mercado",
        tags=['Tipo de Mercados']
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    

    @swagger_auto_schema(
        operation_description="Eliminar tipo de mercado",
        responses={200: TipoMercadoSerializer()},
        operation_summary="Eliminar un tipo de mercado existente",
        tags= ['Tipo de Mercados']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)