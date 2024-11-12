from django.contrib import admin
from plagas.models import Plaga
# Register your models here.
class PlagaAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion')



admin.site.register(Plaga,PlagaAdmin)