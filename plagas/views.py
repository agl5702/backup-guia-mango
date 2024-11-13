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
            "antracnosis": "Se recomienda eliminar las partes afectadas de las plantas y aplicar tratamientos biológicos con extractos naturales como el aceite de neem o el bicarbonato de sodio. Si la situación es grave, se puede considerar el uso de fungicidas sistémicos como el azoxistrobina, pero siempre como último recurso.",
            "cochinilla": "Para controlar la cochinilla, se pueden utilizar depredadores naturales como las mariquitas o insectos benéficos. También puedes aplicar aceites vegetales o jabones insecticidas que son menos agresivos para el medio ambiente. Si la infestación es severa, un insecticida sistémico como el imidacloprid puede ser necesario",
            "eriofidos": "Los eriófidos pueden ser controlados mediante el uso de aceites minerales o aceites esenciales como el de menta, que actúan como repelentes. También puedes aplicar acaricidas naturales a base de tierra de diatomeas. En casos más críticos, el uso de acaricidas químicos como abamectina podría ser necesario.",
            "hormigas": "Utilizar cebos ecológicos para hormigas o trampas caseras con vinagre y azúcar es una forma efectiva de controlarlas. Para plagas más grandes, el monitoreo constante y la eliminación manual de hormigueros pueden ser útiles. Solo si la población se descontrola, se podrían considerar productos químicos como el ácido bórico.",
            "malformación": "La malformación floral o del fruto se puede prevenir mediante la poda adecuada de las ramas afectadas. También se recomienda aplicar tratamientos biológicos preventivos con extractos de plantas. Si los problemas persisten, el uso de fungicidas preventivos, como el tebuconazole, puede ser una opción.",
            "oido": "Para tratar la roya oídio, se recomienda podar las ramas afectadas y aplicar tratamientos naturales como el té de ajo o el bicarbonato de sodio. En caso de una infección grave, un fungicida específico para hongos como el azoxistrobina podría ser necesario, pero siempre en última instancia.",
            "trips": "Los trips pueden ser controlados utilizando depredadores naturales como las ácaros predadores. También se pueden usar trampas pegajosas de color azul o amarillas. En caso de ser necesario, un insecticida de bajo impacto como el spinosad es efectivo para el control de estos insectos",
            "mango_sano": "El mango está en buen estado. Se recomienda mantener buenas prácticas de manejo agrícola, como la poda y la fertilización adecuada. Además, mantener un monitoreo preventivo de plagas y enfermedades puede ayudar a prevenir problemas futuros."
        }

        recomendacion = recomendaciones.get(plaga, "No se han encontrado recomendaciones para esta plaga.")
        return recomendacion.replace("\n", " ")  # Elimina saltos de línea
