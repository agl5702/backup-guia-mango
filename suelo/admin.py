from django.contrib import admin
from suelo.models import FertilidadSuelo,pH,TipoTerreno,TipoSuelo
# Register your models here.
admin.site.register(FertilidadSuelo)
admin.site.register(TipoTerreno)
admin.site.register(pH)
admin.site.register(TipoSuelo)