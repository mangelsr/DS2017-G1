from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.TextField(max_length=50,unique=True)
    password = models.TextField()
    rol = models.TextField(choices=[('Cliente','Cliente'),('Ayudante','Ayudante'),('Administrador','Administrador')])
    #Opciones de ROl, Cliente,Ayudante,Administrador

class Restaurante(models.Model):
    nombre = models.TextField(max_length=50)
    direccion = models.TextField()
    duenio = models.TextField(max_length=50)
    telefono = models.TextField(max_length=15)
    #FK
    ayudante = models.ForeignKey(Usuario,default="",related_name="Usuario")

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
    restaurante = models.ForeignKey(Restaurante, default="", related_name="Restaurante")