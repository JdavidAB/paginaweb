from django.db import models

from django.conf import settings

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='servicios')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.titulo



class Reto(models.Model):
    #id_de_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    id_de_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    minutos_jugados = models.IntegerField(null=True)
    minimo = models.IntegerField(null=True)
    maximo = models.IntegerField(null=True)
    repeticion_niveles = models.IntegerField(null=True)
    engranes = models.IntegerField(null=True)
    duracion_promedio = models.IntegerField(null=True)
    success_promedio = models.IntegerField(null=True)
    a_que_nivel_llego = models.IntegerField(null=True)
    sesion_iniciada_dia = models.IntegerField(null=True)
    sesion_iniciada_mes = models.IntegerField(null=True)