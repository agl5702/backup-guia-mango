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
        
        # Comparación de nutrientes
        for nutriente in nutrientes:
            campo_analisis = NUTRIENTE_MAPPING.get(nutriente.name, nutriente.name.lower())
            valor_analisis = getattr(obj, campo_analisis, None)
            if valor_analisis is not None:
                diferencia = valor_analisis - nutriente.value
                comparacion[nutriente.name] = {
                    'valor_analisis': valor_analisis,
                    'valor_optimo': nutriente.value,
                    'diferencia': diferencia,
                }
            else:
                print(f"No se encontró correspondencia para {nutriente.name}")
        
        # Comparación de pH
        try:
            ph_obj = pH.objects.first()
            if ph_obj:
                diferencia_ph = obj.ph - ph_obj.value
                comparacion['pH'] = {
                    'valor_analisis': obj.ph,
                    'valor_optimo': ph_obj.value,
                    'diferencia': diferencia_ph,
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
            if obj.infiltration_rate is not None and obj.infiltration_rate != drenaje.infiltration_rate:
                comparacion['infiltration_rate'] = {
                    'valor_analisis': obj.infiltration_rate,
                    'valor_referencia': drenaje.infiltration_rate,
                    'diferencia': obj.infiltration_rate - drenaje.infiltration_rate,
                }
            if obj.field_capacity is not None and obj.field_capacity != drenaje.field_capacity:
                comparacion['field_capacity'] = {
                    'valor_analisis': obj.field_capacity,
                    'valor_referencia': drenaje.field_capacity,
                    'diferencia': obj.field_capacity - drenaje.field_capacity,
                }
            if obj.point_wither is not None and obj.point_wither != drenaje.wilting_point:
                comparacion['point_wither'] = {
                    'valor_analisis': obj.point_wither,
                    'valor_referencia': drenaje.wilting_point,
                    'diferencia': obj.point_wither - drenaje.wilting_point,
                }
            if obj.permeability is not None and obj.permeability != drenaje.permeability:
                comparacion['permeability'] = {
                    'valor_analisis': obj.permeability,
                    'valor_referencia': drenaje.permeability,
                    'diferencia': obj.permeability - drenaje.permeability,
                }
            if obj.porosity is not None and obj.porosity != drenaje.porosity:
                comparacion['porosity'] = {
                    'valor_analisis': obj.porosity,
                    'valor_referencia': drenaje.porosity,
                    'diferencia': obj.porosity - drenaje.porosity,
                }

        return comparacion

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['comparacion_nutrientes'] = self.get_comparacion_nutrientes(instance)
        representation['comparacion_drenaje'] = self.get_comparacion_drenaje(instance)
        return representation
