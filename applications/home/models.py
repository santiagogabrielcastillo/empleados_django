from django.db import models

# Create your models here.
class Prueba(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.titulo} - {self.subtitulo}'

    def __unicode__(self):
        return 
