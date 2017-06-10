from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Restaurant(models.Model):
    name = models.TextField(max_length=50)
    adress = models.TextField()
    owner = models.TextField(max_length=50)
    phone_number = models.TextField(max_length=15)
    def __unicode__(self):
        return self.name

class Profile(models.Model):
    role = models.TextField(choices=[('Cliente','Cliente'),('Ayudante','Ayudante'),('Administrador','Administrador')])
    #Opciones de ROL, Cliente,Ayudante,Administrador
    #FK
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, null=True, blank=True)
    def __unicode__(self):
        return self.user.username

class Dish(models.Model):
    name = models.TextField(max_length=50)
    ingredients = models.TextField()
    image = models.TextField()
    description = models.TextField()
    dish_choice = models.TextField(choices=[('Aperitivo','Aperitivo'),('Plato Fuerte','Plato Fuerte'),('Postre','Postre')])
    #Aperitivo, plato fuerte y la otra cosa
    temperature = models.TextField(choices=[('Frio','Frio'),('Caliente','Caliente')])
    #Caliente o frio
    # FK
    restaurant = models.ForeignKey(Restaurant)
    def __unicode__(self):
        return self.name
