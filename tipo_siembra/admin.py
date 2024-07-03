from django.contrib import admin
from tipo_siembra.models import TipoSiembra 
# Register your models here.
class TipoSiembraAdmin(admin.ModelAdmin):
    
    list_display=['name','description']
    search_fields=['name']
    

admin.site.register(TipoSiembra,TipoSiembraAdmin)