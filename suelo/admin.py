from django.contrib import admin
from suelo.models import FertilidadSuelo,pH,TipoSuelo,DrenajeSuelo,TexturaSuelo
# Register your models here.
admin.site.register(FertilidadSuelo)
admin.site.register(pH)
admin.site.register(TipoSuelo)
admin.site.register(DrenajeSuelo)
admin.site.register(TexturaSuelo)