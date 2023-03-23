from django.db import models

class Circulares(models.Model):
    link = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    intro = models.CharField(max_length=255)
    anexo = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateField()

    class Meta:
        verbose_name = 'Circular'
        verbose_name_plural = 'Circulares'

    def __str__(self):
        return self.titulo
