from django.db import models

# Create your models here.
class Informes(models.Model):
    report_type = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    date = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Informes'

    def __str__(self):
        return self.name

