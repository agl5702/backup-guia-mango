from django.contrib import admin
from hectareas.models import Hectareas
# Register your models here.
class HectareasAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'description', 'number_trees')

admin.site.register(Hectareas,HectareasAdmin)