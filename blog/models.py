from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    
    nombre = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre
    

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True) # la imagen se suba en blog y las condiciones true son para que si no hay imgn se quede en blanco
    autor = models.ForeignKey(User, on_delete=models.CASCADE) # ancla los blogs a los usuarios y si un user es eliminado los blogs se eliminaran en cascada
    categorias = models.ManyToManyField(Categoria)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.titulo