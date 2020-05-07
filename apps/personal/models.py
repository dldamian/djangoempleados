from django.db import models
from apps.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleado'

    def __str__(self):
        return str(self.id) + ' - ' + self.habilidad


class Empleado(models.Model):
    '''Modelo para tabla empleado'''

    tipos_trabajos = (
        ('0','Contador'),
        ('1','Administrador'),
        ('2','Economista'),
        ('3','Otro')
    )

    primer_nombre = models.CharField('Nombres', max_length=60)
    apellidos = models.CharField('Apellidos', max_length=60)
    nombre_completo = models.CharField(
        'Nombre Completo',
        max_length=120,
        blank=True
    )
    trabajo = models.CharField('Trabajo', max_length=1, choices=tipos_trabajos)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidad = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()
    #imagen = models.ImageField(upload='empleado', blank=True, null=True)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Mis Empleados'
        ordering = ['primer_nombre','apellidos']
        unique_together = ('primer_nombre','departamento')
    
    def __str__(self):
        return str(self.id) + ' - ' + self.primer_nombre + ' - ' + self.apellidos
