from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Restaurante(models.Model):
    nombre = models.TextField(max_length=50)
    direccion = models.TextField()
    duenio = models.TextField(max_length=50)
    telefono = models.TextField(max_length=15)
    def __unicode__(self):
        return unicode(self.nombre)

class Perfil(models.Model):
    rol = models.TextField(choices=[('Cliente','Cliente'),('Ayudante','Ayudante'),('Administrador','Administrador')])
    #Opciones de ROL, Cliente,Ayudante,Administrador
    #FK
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, null=True, blank=True)
    def __unicode__(self):
        return unicode(self.user.username)

class Platillo(models.Model):
    nombre = models.TextField(max_length=50)
    ingredientes = models.TextField()
    imagen = models.TextField()
    descripcion = models.TextField()
    tipo = models.TextField(choices=[('Aperitivo','Aperitivo'),('Plato Fuerte','Plato Fuerte'),('Postre','Postre')])
    #Aperitivo, plato fuerte y la otra cosa
    temperatura = models.TextField(choices=[('Frio','Frio'),('Caliente','Caliente')])
    #Caliente o frio
    # FK
    restaurante = models.ForeignKey(Restaurante)
