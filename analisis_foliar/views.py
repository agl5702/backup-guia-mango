from rest_framework import viewsets
from analisis_foliar.models import AnalisisFoliar
from analisis_foliar.serializers import AnalisisFoliarSerializer
from drf_yasg.utils import swagger_auto_schema # type: ignore
from drf_yasg import openapi # type: ignore

# Create your views here.
class AnalisisFoliarView(viewsets.ModelViewSet):
    
    serializer_class = AnalisisFoliarSerializer
    queryset = AnalisisFoliar.objects.all()

    @swagger_auto_schema(
        operation_description="Obtener todos los análisis foliares",
        responses={200: AnalisisFoliarSerializer(many=True)},
        operation_summary="Obten una Lista de los análisis foliares",
        tags= ['Análisis Foliar']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtener un análisis foliares por su ID.",
        responses={200: AnalisisFoliarSerializer()},
        operation_summary="Obeter un análisis foliares por ID",
        tags= ['Análisis Foliar']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Crear un análisis foliar",
        responses={200: AnalisisFoliarSerializer()},
        operation_summary="Crea un análisis foliar",
        tags= ['Análisis Foliar']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualizar análisis foliar por ID",
        responses={200: AnalisisFoliarSerializer()},
        operation_summary="Actualiza un análisis foliar por ID",
        tags= ['Análisis Foliar']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Actualizar parcialmente un análisis foliar",
        responses={200: AnalisisFoliarSerializer()},
        operation_summary="Actualizar parcialmente un análisis foliar",
        tags=['Análisis Foliar']
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Eliminar un análisis foliar por ID.",
        responses={204: "No content"},
        operation_summary="Elimina un análisis foliar por ID",
        tags= ['Análisis Foliar']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)