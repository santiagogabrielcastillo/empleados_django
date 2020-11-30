from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField


class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
        ordering = ['habilidad']
        
    def __str__(self):
        return f'{self.habilidad}'

    def __unicode__(self):
        return 


class Empleado(models.Model):
    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    job_choices = [
        ('0', 'Contador'), 
        ('1','Abogado'), 
        ('2', 'Economista'), 
        ('3', 'Ingeniero')
        ]
    full_name = models.CharField(
        'Nombres completos',
        max_length=120,
        blank=True
    )
    job = models.CharField('Trabajo', max_length=1, choices=job_choices)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField('Avatar', upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    # cv = RichTextField()
    
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['id']
    
    def __str__(self):
        return f'({self.id}) - {self.first_name} {self.last_name}'

    def __unicode__(self):
        return 

