from django.db import models

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corto', max_length=7, unique=True)
    anulate = models.BooleanField('Anulado', default=False)


    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.short_name})'

    def __unicode__(self):
        return 

