from rest_framework import serializers
from analisis_suelo.models import AnalisisSuelo
from suelo.models import FertilidadSuelo, pH, DrenajeSuelo

# Mapeo actualizado para los nutrientes en kg/ha
NUTRIENTE_MAPPING = {
    'Nitrógeno': 'nh4_kg_per_ha',
    'Fósforo': 'phosphorus_kg_per_ha',
    'Potasio': 'potassium_kg_per_ha',
    'Calcio': 'calcium_kg_per_ha',
    'Magnesio': 'magnesium_kg_per_ha',
    'Azufre': 'sulfur_kg_per_ha',
    'Hierro': 'iron_kg_per_ha',
    'Manganeso': 'manganese_kg_per_ha',
    'Zinc': 'zinc_kg_per_ha',
    'Cobre': 'copper_kg_per_ha',
    'Molibdeno': 'molybdenum_kg_per_ha',
    'Boro': 'boron_kg_per_ha'
}

def format_decimal(value):
    # Redondear a dos decimales y agregar "kg/ha"
    rounded_value = round(value, 2)
    # Considerar diferencias menores a 0.01 como 0
    if abs(rounded_value) < 0.01:
        return "0.00 kg/ha"
    return f"{rounded_value:.2f} kg/ha"

# Recomendaciones específicas para cada nutriente
RECOMENDACIONES = {
    "pH": {
        "OPTIMO": "El nivel de PH es adecuado para el desarrollo del mango. Mantener las prácticas actuales.",
        "BAJO": "El PH está bajo. Se recomienda aplicar fertilizante que contenga nitrógeno para mejorar el crecimiento y desarrollo de las frutas.",
        "ELEVADO": "El nivel de PH es alto. Reducir la aplicación de fertilizantes nitrogenados para evitar un crecimiento excesivo y problemas en la calidad de las frutas."
    },
    "Nitrógeno": {
        "OPTIMO": "El nivel de nitrógeno es adecuado para el desarrollo del mango. Mantener las prácticas actuales.",
        "BAJO": "El nitrógeno está bajo. Se recomienda aplicar fertilizante que contenga nitrógeno para mejorar el crecimiento y desarrollo de las frutas.",
        "ELEVADO": "El nivel de nitrógeno es alto. Reducir la aplicación de fertilizantes nitrogenados para evitar un crecimiento excesivo y problemas en la calidad de las frutas."
    },
    "Fósforo": {
        "OPTIMO": "El fósforo está en niveles óptimos. Continuar con las prácticas actuales de fertilización para asegurar un buen desarrollo de las raíces y la floración.",
        "BAJO": "El fósforo está bajo. Aplicar fertilizantes ricos en fósforo para promover un buen desarrollo radicular y una floración saludable.",
        "ELEVADO": "El fósforo está elevado. Evitar el exceso de fertilización para prevenir toxicidades que pueden afectar el crecimiento y la calidad del fruto."
    },
    "Potasio": {
        "OPTIMO": "El potasio está en niveles ideales para el mango. No se requieren ajustes en la fertilización. El potasio contribuye a la resistencia a enfermedades y al desarrollo de frutos.",
        "BAJO": "El potasio está bajo. Considerar aplicar fertilizantes con potasio para mejorar la resistencia a enfermedades y la calidad de los frutos.",
        "ELEVADO": "El nivel de potasio es alto. Reducir la aplicación de fertilizantes potásicos para evitar problemas de absorción de otros nutrientes y posibles efectos adversos en la calidad del fruto."
    },
    "Calcio": {
        "OPTIMO": "El calcio está en niveles adecuados. Mantener las prácticas actuales para asegurar una buena calidad de los frutos y una estructura celular saludable.",
        "BAJO": "El calcio está bajo. Aplicar fertilizantes que contengan calcio para mejorar la calidad de los frutos y evitar problemas como la pudrición apical.",
        "ELEVADO": "El nivel de calcio es alto. Reducir la aplicación de fertilizantes con calcio para evitar posibles desequilibrios con otros nutrientes."
    },
    "Magnesio": {
        "OPTIMO": "El magnesio está en niveles óptimos. Continuar con las prácticas actuales para mantener una buena producción de clorofila y crecimiento.",
        "BAJO": "El magnesio está bajo. Aplicar fertilizantes que contengan magnesio para prevenir clorosis y asegurar un buen desarrollo de las hojas.",
        "ELEVADO": "El nivel de magnesio es alto. Reducir la aplicación de fertilizantes con magnesio para evitar problemas de absorción de otros nutrientes."
    },
    "Azufre": {
        "OPTIMO": "El azufre está en niveles adecuados. Mantener las prácticas actuales para apoyar la síntesis de aminoácidos y proteínas.",
        "BAJO": "El azufre está bajo. Aplicar fertilizantes que contengan azufre para apoyar el crecimiento y la calidad del fruto.",
        "ELEVADO": "El nivel de azufre es alto. Reducir la aplicación de fertilizantes con azufre para evitar problemas de toxicidad y desequilibrio de nutrientes."
    },
    "Hierro": {
        "OPTIMO": "El hierro está en niveles adecuados. Continuar con las prácticas actuales para asegurar un buen crecimiento y coloración de las hojas.",
        "BAJO": "El hierro está bajo. Aplicar fertilizantes que contengan hierro para prevenir la clorosis y mejorar la fotosíntesis.",
        "ELEVADO": "El nivel de hierro es alto. Reducir la aplicación de fertilizantes con hierro para evitar posibles problemas de toxicidad."
    },
    "Manganeso": {
        "OPTIMO": "El manganeso está en niveles adecuados. Mantener las prácticas actuales para asegurar una buena fotosíntesis y metabolismo.",
        "BAJO": "El manganeso está bajo. Aplicar fertilizantes que contengan manganeso para prevenir problemas de crecimiento y clorosis.",
        "ELEVADO": "El nivel de manganeso es alto. Reducir la aplicación de fertilizantes con manganeso para evitar toxicidades y desequilibrios nutricionales."
    },
    "Zinc": {
        "OPTIMO": "El zinc está en niveles óptimos. Continuar con las prácticas actuales para mantener una buena estructura celular y desarrollo de los frutos.",
        "BAJO": "El zinc está bajo. Aplicar fertilizantes que contengan zinc para prevenir problemas de crecimiento y desarrollo de los frutos.",
        "ELEVADO": "El nivel de zinc es alto. Reducir la aplicación de fertilizantes con zinc para evitar efectos adversos en la salud de la planta."
    },
    "Cobre": {
        "OPTIMO": "El cobre está en niveles adecuados. Mantener las prácticas actuales para apoyar el crecimiento y la salud de la planta.",
        "BAJO": "El cobre está bajo. Aplicar fertilizantes que contengan cobre para prevenir problemas de desarrollo y enfermedades.",
        "ELEVADO": "El nivel de cobre es alto. Reducir la aplicación de fertilizantes con cobre para evitar toxicidades y problemas en el crecimiento."
    },
    "Molibdeno": {
        "OPTIMO": "El molibdeno está en niveles adecuados. Continuar con las prácticas actuales para apoyar el metabolismo y la asimilación de nitrógeno.",
        "BAJO": "El molibdeno está bajo. Aplicar fertilizantes que contengan molibdeno para mejorar la eficiencia en el uso del nitrógeno.",
        "ELEVADO": "El nivel de molibdeno es alto. Reducir la aplicación de fertilizantes con molibdeno para evitar desequilibrios nutricionales."
    },
    "Boro": {
        "OPTIMO": "El boro está en niveles adecuados. Mantener las prácticas actuales para asegurar un buen desarrollo de las flores y frutos.",
        "BAJO": "El boro está bajo. Aplicar fertilizantes que contengan boro para prevenir problemas de cuajado y desarrollo de los frutos.",
        "ELEVADO": "El nivel de boro es alto. Reducir la aplicación de fertilizantes con boro para evitar problemas de toxicidad y efectos adversos en la calidad del fruto."
    }
}
class AnalisisSueloSerializer(serializers.ModelSerializer):
    comparacion_nutrientes = serializers.SerializerMethodField()
    comparacion_drenaje = serializers.SerializerMethodField()
    soil_type = serializers.StringRelatedField()
    soil_texture = serializers.StringRelatedField()
    usuario = serializers.StringRelatedField()

    class Meta:
        model = AnalisisSuelo
        fields = '__all__'

    def create(self,validated_data):

        # Obtener el usuario autenticado
        usuario = self.context['request'].user
                # Asignar automáticamente el usuario al crear un nuevo torneo
        validated_data['usuario'] = usuario
                # Crear y devolver el objeto Torneo
        return AnalisisSuelo.objects.create(**validated_data)

    def get_comparacion_nutrientes(self, obj):
        nutrientes = FertilidadSuelo.objects.all()
        comparacion = {}
        
        # Comparación de nutrientes
        for nutriente in nutrientes:
            campo_analisis = NUTRIENTE_MAPPING.get(nutriente.name)
            
            if campo_analisis:
                valor_analisis = getattr(obj, campo_analisis, None)
                if valor_analisis is not None:
                    # Lógica de comparación
                    if valor_analisis < nutriente.min_value:
                        diferencia = format_decimal(valor_analisis - nutriente.min_value)
                        estado = "BAJO"
                    elif valor_analisis > nutriente.max_value:
                        diferencia = format_decimal(valor_analisis - nutriente.max_value)
                        estado = "ELEVADO"
                    else:
                        diferencia = format_decimal(0)
                        estado = "OPTIMO"
                    
                    comparacion[nutriente.name] = {
                        'valor_analisis': format_decimal(valor_analisis),
                        'valor_minimo': format_decimal(nutriente.min_value),
                        'valor_maximo': format_decimal(nutriente.max_value),
                        'diferencia': diferencia,
                        'estado': estado,
                        'recomendacion': RECOMENDACIONES.get(nutriente.name, {}).get(estado, "Recomendación no disponible"),  # Recomendación específica
                    }
                else:
                    print(f"No se encontró valor para {campo_analisis} en la instancia de AnalisisSuelo.")
            else:
                print(f"No se encontró mapeo para el nutriente {nutriente.name}.")
        
        # Comparación de pH
        try:
            ph_obj = pH.objects.first()
            if ph_obj:
                if obj.ph < ph_obj.min_value:
                    diferencia_ph = format_decimal(obj.ph - ph_obj.min_value)
                    estado_ph = "BAJO"
                elif obj.ph > ph_obj.max_value:
                    diferencia_ph = format_decimal(obj.ph - ph_obj.max_value)
                    estado_ph = "ELEVADO"
                else:
                    diferencia_ph = format_decimal(0)
                    estado_ph = "OPTIMO"

                comparacion['pH'] = {
                    'valor_analisis': format_decimal(obj.ph),
                    'valor_minimo': format_decimal(ph_obj.min_value),
                    'valor_maximo': format_decimal(ph_obj.max_value),
                    'diferencia': diferencia_ph,
                    'estado': estado_ph,
                    'recomendacion': RECOMENDACIONES.get('pH', {}).get(estado_ph, "Recomendación no disponible"),  # Recomendación específica para pH
                }
            else:
                print("No se encontró objeto de pH para comparar.")
        except pH.DoesNotExist:
            print("No se encontró objeto de pH para comparar.")
        
        return comparacion

    def get_comparacion_drenaje(self, obj):
        drenaje = DrenajeSuelo.objects.first()
        comparacion = {}

        if drenaje:
            campos_drenaje = [
                ('infiltration_rate', 'infiltration_rate'),
                ('field_capacity', 'field_capacity'),
                ('point_wilting', 'wilting_point'),
                ('permeability', 'permeability'),
                ('porosity', 'porosity')
            ]

            for campo_obj, campo_drenaje in campos_drenaje:
                valor_obj = getattr(obj, campo_obj, None)
                valor_drenaje = getattr(drenaje, campo_drenaje, None)
                
                if valor_obj is not None and valor_drenaje is not None:
                    diferencia = format_decimal(valor_obj - valor_drenaje)
                    comparacion[campo_obj] = {
                        'valor_analisis': format_decimal(valor_obj),
                        'valor_referencia': format_decimal(valor_drenaje),
                        'diferencia': diferencia,
                    }

        return comparacion

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(f"Valores en el serializador - Potasio: {representation.get('potassium_kg_per_ha')}, Calcio: {representation.get('calcium_kg_per_ha')}, Magnesio: {representation.get('magnesium_kg_per_ha')}, Sodio: {representation.get('sodium_kg_per_ha')}")
        representation['comparacion_nutrientes'] = self.get_comparacion_nutrientes(instance)
        representation['comparacion_drenaje'] = self.get_comparacion_drenaje(instance)
        return representation

    
