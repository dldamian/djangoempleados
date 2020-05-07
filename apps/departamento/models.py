from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField('Nombre',max_length=100)
    nombre_corto = models.CharField('Nombre Corto',max_length=20, unique=True)
    esta_activo = models.BooleanField('Esta Activo', default=True)

    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Áreas de la Empresa'
        ordering = ['nombre']
        unique_together = ('nombre','nombre_corto')
    
    def __str__(self):
        return str(self.id) + ' - ' + self.nombre + ' - ' + self.nombre_corto