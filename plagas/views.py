from rest_framework import viewsets
from plagas.models import Plaga
from rest_framework.permissions import IsAuthenticated
from plagas.serializers import PlagaSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework.decorators import action
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from rest_framework.parsers import MultiPartParser, FormParser
import os
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

import django
django.setup() 

# Cargar el modelo previamente entrenado
model = tf.keras.models.load_model(settings.MODEL_PATH)

# Función para cargar y preprocesar la imagen de prueba
def cargar_imagen(img_path, img_height=128, img_width=128):
    img = image.load_img(img_path, target_size=(img_height, img_width))
    img_array = image.img_to_array(img)  # Convertir la imagen a un array
    img_array = np.expand_dims(img_array, axis=0)  # Añadir una dimensión para el batch
    img_array = img_array / 255.0  # Normalizar la imagen
    return img_array

class PlagaView(viewsets.ModelViewSet):
    serializer_class = PlagaSerializer
    queryset = Plaga.objects.all()
    permission_classes = [IsAuthenticated]
    # Establecer los parsers para permitir la carga de archivos
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        operation_description="Obtener todas las plagas",
        responses={201: PlagaSerializer()},
        operation_summary="Obtener una lista de todas las plagas",
        tags=['Plagas']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Obtener una plaga por ID",
        responses={200: PlagaSerializer()},
        operation_summary="Obtener una plaga por ID"
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Crear una nueva plaga",
        responses={201: PlagaSerializer()},
        operation_summary="Crear una nueva plaga"
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Actualizar una plaga por ID",
        responses={200: PlagaSerializer()},
        operation_summary="Actualizar una plaga por ID"
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Actualizar parcialmente una plaga",
        responses={200: PlagaSerializer()},
        operation_summary="Actualizar parcialmente una plaga"
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Eliminar una plaga por ID",
        responses={204: None},
        operation_summary="Eliminar una plaga por ID"
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    # Acción personalizada para hacer la predicción
    @action(detail=False, methods=['post'], serializer_class=PlagaSerializer)
    @swagger_auto_schema(
        operation_description="Predecir la plaga basada en la imagen proporcionada",
        responses={200: PlagaSerializer()},
        operation_summary="Hacer una predicción sobre qué plaga puede estar presente"
    )
    def predict(self, request):
        # Verifica si la imagen ha sido enviada
        if 'image' not in request.FILES:
            return Response({"error": "No se ha enviado una imagen."}, status=400)

        image_file = request.FILES['image']
        
        # Guardar temporalmente la imagen para procesarla
        img_path = f'temp_{image_file.name}'
        with open(img_path, 'wb') as f:
            for chunk in image_file.chunks():
                f.write(chunk)
        
        # Preprocesar la imagen
        test_img = cargar_imagen(img_path)

        # Hacer la predicción
        pred = model.predict(test_img)

        # Obtener la clase con mayor probabilidad
        predicted_class = np.argmax(pred, axis=1)

        # Obtener el nombre de la clase predicha
        class_names = list(os.listdir('plague_dataset'))  # Obtener nombres de las carpetas (clases)
        predicted_class_name = class_names[predicted_class[0]]

        # Eliminar el archivo temporal
        os.remove(img_path)

        return Response({
            "prediccion": predicted_class_name,
            "probabilidades": [
                {"clase": class_names[i], "probabilidad": prob*100}
                for i, prob in enumerate(pred[0])
            ]
        })
