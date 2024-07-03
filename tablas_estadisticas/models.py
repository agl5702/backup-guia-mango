from django.db import models

# Create your models here.
class TablasEstadisticas(models.Model):
    name = models.CharField(max_length=45)
    type_of_statistics = models.CharField(max_length=45)
    description = models.CharField(max_length=45)

    def __str__(self):
        return self.name