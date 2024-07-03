from django.contrib import admin
from nutrientes.models import Nutrientes,pH,TipoTerreno,TipoSuelo
# Register your models here.
admin.site.register(Nutrientes)
admin.site.register(TipoTerreno)
admin.site.register(pH)
admin.site.register(TipoSuelo)