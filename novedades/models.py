from django.db import models

class Novedades(models.Model):
    link = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    intro = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Novedad'
        verbose_name_plural = 'Novedades'

    def __str__(self):
        return self.titulo