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
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"

class Profile(models.Model):
    role = models.CharField(max_length=20,choices=[('Cliente','Cliente'),('Ayudante','Ayudante'),('Administrador','Administrador')],default='C',null=False,blank=False)
    #Opciones de ROL, Cliente,Ayudante,Administrador
    #FK
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, null=True, blank=True)
    def __unicode__(self):
        return self.user.username
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

class Dish(models.Model):
    name = models.TextField(max_length=50)
    ingredients = models.TextField()
    image = models.TextField()
    description = models.TextField()
    dish_choice = models.CharField(max_length=20,choices=[('Aperitivo','Aperitivo'),('Plato Fuerte','Plato Fuerte'),('Postre','Postre')],default='A',null=False,blank=False)
    #Aperitivo, plato fuerte y la otra cosa
    temperature = models.CharField(max_length=20,choices=[('Frio','Frio'),('Caliente','Caliente')],default='C',null=False,blank=False)
    #Caliente o frio
    # FK
    restaurant = models.ForeignKey(Restaurant)
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"
