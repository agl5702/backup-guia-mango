from django.db import models

# Create your models here.
class Informes(models.Model):
    report_type = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

