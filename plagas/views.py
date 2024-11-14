from rest_framework import viewsets
from plagas.models import Plaga
from rest_framework.permissions import IsAuthenticated
from plagas.serializers import PlagaSerializer
from drf_yasg.utils import swagger_auto_schema
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

        # Recomendar acciones basadas en la predicción
        recomendaciones = self.obtener_recomendaciones(predicted_class_name)

        return Response({
            "prediccion": predicted_class_name,
            "recomendaciones": recomendaciones
        })

    def obtener_recomendaciones(self, plaga):
        recomendaciones = {
            "antracnosis": "1. Mejorar la circulación de aire mediante una poda adecuada para reducir la densidad de ramas y minimizar la humedad en el árbol. 2. Eliminar y destruir hojas y frutos infectados caídos o en el árbol para reducir la fuente de esporas y prevenir la propagación.",
            "cochinilla": "1. Introducir insectos depredadores naturales, como mariquitas, que se alimentan de las cochinillas y ayudan a controlar su población. 2. Usar un paño húmedo o agua a presión para remover manualmente las cochinillas de ramas y frutos, especialmente en árboles pequeños.",
            "eriofidos": "1. Podar ramas afectadas para reducir la población de eriofidos y mejorar la salud general del árbol. 2. Fomentar la presencia de ácaros depredadores que actúan como controladores naturales de los eriofidos en el cultivo.",
            "hormigas": "1. Instalar barreras físicas adhesivas alrededor del tronco para evitar que las hormigas suban y se asocien con plagas como las cochinillas. 2. Eliminar los nidos de hormigas en los alrededores mediante métodos físicos, como el uso de agua caliente, sin dañar el ecosistema del huerto.",
            "malformacion": "1. Eliminar y destruir flores y brotes deformados al detectarlos para reducir la propagación de la malformación a otros brotes sanos. 2. Mantener una adecuada higiene en el huerto retirando restos vegetales cercanos al árbol, los cuales pueden albergar agentes causantes de malformación.",
            "oido": "1. Realizar una poda para mejorar la exposición al sol en el interior del árbol, reduciendo la humedad que favorece el desarrollo del oídio. 2. Evitar la plantación de especies susceptibles al oídio cerca del mango, especialmente aquellas como cucurbitáceas, para reducir la presión de la enfermedad en el área.",
            "trips": "1 .Colocar trampas adhesivas azules alrededor del cultivo para capturar trips adultos y reducir su número en el árbol. 2. Implementar riego por aspersión ocasionalmente para crear un ambiente menos favorable para los trips y desalojarlos de las hojas.",
            "mango_sano": "El mango está en buen estado. Se recomienda mantener buenas prácticas de manejo agrícola, como la poda y la fertilización adecuada. Además, mantener un monitoreo preventivo de plagas y enfermedades puede ayudar a prevenir problemas futuros."
        }

        recomendacion = recomendaciones.get(plaga, "No se han encontrado recomendaciones para esta plaga.")
        return recomendacion.replace("\n", " ")  # Elimina saltos de línea