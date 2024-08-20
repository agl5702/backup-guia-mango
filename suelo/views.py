from rest_framework import viewsets
from suelo.models import FertilidadSuelo,pH,TipoSuelo
from suelo.serializers import FertilidadSueloSerializer,pHSerializer,TipoSueloSerializer
from drf_yasg.utils import swagger_auto_schema 
from drf_yasg import openapi

# Create your views here.
class FertilidadSueloView(viewsets.ModelViewSet):
    
    serializer_class = FertilidadSueloSerializer
    queryset = FertilidadSuelo.objects.all()

    @swagger_auto_schema(
        operation_description="Obtener todos los nutrientes",
        responses={200: FertilidadSueloSerializer(many=True)},
        operation_summary="Lista de nutrientes del suelo",
        tags= ['Nutrientes']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtener un nutriente por su ID.",
        responses={200: FertilidadSueloSerializer()},
        operation_summary="Obeter nutriene por ID",
        tags= ['Nutrientes']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Crear un nuevo nutriente",
        responses={200: FertilidadSueloSerializer()},
        operation_summary="Crea un nutriente",
        tags= ['Nutrientes']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualizar nutriente por ID",
        responses={200: FertilidadSueloSerializer()},
        operation_summary="Actualiza un nutriente por ID",
        tags= ['Nutrientes']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Actualizar parcialmente un nutriente",
        responses={200: FertilidadSueloSerializer()},
        operation_summary="Actualizar parcialmente un nutriente",
        tags=['Nutrientes']
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Eliminar un nutriente por ID.",
        responses={204: "No content"},
        operation_summary="Elimina un nutriente por ID",
        tags= ['Nutrientes']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)



    
class pHView(viewsets.ModelViewSet):

    serializer_class = pHSerializer
    queryset = pH.objects.all()
    
    @swagger_auto_schema(
        operation_description="Obtener el valor del PH",
        responses={200: pHSerializer(many=True)},
        operation_summary="Lista de los valores del PH",
        tags= ['PH']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtener el PH por su ID.",
        responses={200: pHSerializer()},
        operation_summary="Obeter PH por ID",
        tags= ['PH']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Crear un nuevo valor de PH",
        responses={200: pHSerializer()},
        operation_summary="Crea un PH con nuevo valor",
        tags= ['PH']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualizar el valor del PH por ID",
        responses={200: pHSerializer()},
        operation_summary="Actualiza el valor del PH por ID",
        tags= ['PH']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Actualizar parcialmente el valor del PH",
        responses={200: pHSerializer()},
        operation_summary="Actualizar parcialmente el valor del PH",
        tags=['PH']
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Eliminar el valor del PH por ID.",
        responses={204: "No content"},
        operation_summary="Elimina el valor del PH por ID",
        tags= ['PH']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)



class TipoSueloView(viewsets.ModelViewSet):

    serializer_class= TipoSueloSerializer
    queryset = TipoSuelo.objects.all()

    @swagger_auto_schema(
        operation_description="Obtener los tipos de suelos",
        responses={200: TipoSueloSerializer(many=True)},
        operation_summary="Lista de los tipos de suelos",
        tags= ['Tipos de Suelos']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtener tipo de suelo por ID.",
        responses={200: TipoSueloSerializer()},
        operation_summary="Obeter tipo de suelo por ID",
        tags= ['Tipos de Suelos']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Crear un nuevo tipo de suelo",
        responses={200: TipoSueloSerializer()},
        operation_summary="Crea un nuevo tipo de suelo",
        tags= ['Tipos de Suelos']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualizar el tipo de suelo ID",
        responses={200: TipoSueloSerializer()},
        operation_summary="Actualiza el tipo de suelo ID",
        tags= ['Tipos de Suelos']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Actualizar parcialmente el tipo de suelo",
        responses={200: TipoSueloSerializer()},
        operation_summary="Actualizar parcialmente el tipo de suelo",
        tags=['Tipos de Suelos']
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Eliminar el tipo de suelo por ID.",
        responses={204: "No content"},
        operation_summary="Elimina el tipo de suelo por ID",
        tags= ['Tipos de Suelos']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)