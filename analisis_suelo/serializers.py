from rest_framework import serializers
from analisis_suelo.models import AnalisisSuelo
from suelo.models import FertilidadSuelo,pH,DrenajeSuelo


NUTRIENTE_MAPPING = {
    'Nitrógeno': 'nitrogen',
    'Fósforo': 'phosphorus',
    'Potasio': 'potassium',
    'Calcio': 'calcium',
    'Magnesio': 'magnesium',
    'Azufre': 'sulfur',
    'Hierro': 'iron',
    'Manganeso': 'manganese',
    'Zinc': 'zinc',
    'Cobre': 'copper',
    'Molibdeno': 'molybdenum',
    'Boro': 'boron'
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

    def get_comparacion_nutrientes(self, obj):
        nutrientes = FertilidadSuelo.objects.all()
        comparacion = {}
        
        for nutriente in nutrientes:
            campo_analisis = NUTRIENTE_MAPPING.get(nutriente.name, nutriente.name.lower())
            valor_analisis = getattr(obj, campo_analisis, None)
            if valor_analisis is not None:
                if valor_analisis < nutriente.min_value:
                    diferencia = valor_analisis - nutriente.min_value
                    estado = "BAJO"
                elif valor_analisis > nutriente.max_value:
                    diferencia = valor_analisis - nutriente.max_value
                    estado = "ELEVADO"
                else:
                    diferencia = 0
                    estado = "OPTIMO"
                
                comparacion[nutriente.name] = {
                    'valor_analisis': valor_analisis,
                    'valor_minimo': nutriente.min_value,
                    'valor_maximo': nutriente.max_value,
                    'diferencia': diferencia,
                    'estado': estado,
                }
            else:
                print(f"No se encontró correspondencia para {nutriente.name}")
        
        # Comparación de pH
        try:
            ph_obj = pH.objects.first()
            if ph_obj:
                if obj.ph < ph_obj.min_value:
                    diferencia_ph = obj.ph - ph_obj.min_value
                    estado_ph = "BAJO"
                elif obj.ph > ph_obj.max_value:
                    diferencia_ph = obj.ph - ph_obj.max_value
                    estado_ph = "ELEVADO"
                else:
                    diferencia_ph = 0
                    estado_ph = "OPTIMO"
                
                comparacion['pH'] = {
                    'valor_analisis': obj.ph,
                    'valor_minimo': ph_obj.min_value,
                    'valor_maximo': ph_obj.max_value,
                    'diferencia': diferencia_ph,
                    'estado': estado_ph,
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
                ('point_wither', 'wilting_point'),
                ('permeability', 'permeability'),
                ('porosity', 'porosity')
            ]

            for campo_obj, campo_drenaje in campos_drenaje:
                valor_obj = getattr(obj, campo_obj, None)
                valor_drenaje = getattr(drenaje, campo_drenaje, None)
                
                if valor_obj is not None and valor_drenaje is not None:
                    diferencia = valor_obj - valor_drenaje
                    comparacion[campo_obj] = {
                        'valor_analisis': valor_obj,
                        'valor_referencia': valor_drenaje,
                        'diferencia': diferencia,
                    }

        return comparacion

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(f"Valores en el serializador - Potasio: {representation.get('potassium')}, Calcio: {representation.get('calcium')}, Magnesio: {representation.get('magnesium')}, Sodio: {representation.get('sodium')}")
        representation['comparacion_nutrientes'] = self.get_comparacion_nutrientes(instance)
        representation['comparacion_drenaje'] = self.get_comparacion_drenaje(instance)
        return representation
