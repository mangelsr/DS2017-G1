from django.db import models
from django.contrib.auth.models import User
from .choices import *
#from django.db.models.signals import post_delete
#from django.dispatch import receiver


class Restaurant(models.Model):
    name = models.TextField(max_length=50)
    address = models.TextField()
    owner = models.TextField(max_length=50)
    phone_number = models.TextField(max_length=15)
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"

class Role(models.Model):
    name = models.TextField(max_length=50)
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

class Profile(models.Model):
    role = models.ForeignKey(Role,null=False,blank=False)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, related_name='profiles',null=True, blank=True, help_text='Solo necesario si el rol es Ayudante')
    def __unicode__(self):
        return self.user.username
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

class DishType(models.Model):
    name = models.TextField(max_length=25)
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"

class DishTemperature(models.Model):
    name = models.TextField(max_length=25)
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Temperatura"
        verbose_name_plural = "Temperaturas"

class DishCategory(models.Model):
    name = models.TextField(max_length=30)
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Dish(models.Model):
    name = models.TextField(max_length=50)
    ingredients = models.TextField()
    image = models.ImageField(upload_to='photos/',null=True)
    description = models.TextField()
    dish_choice = models.ForeignKey(DishType)
    dish_category = models.ForeignKey(DishCategory,null=True)
    temperature = models.ForeignKey(DishTemperature)
    restaurant = models.ForeignKey(Restaurant)
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Dish, self).delete(*args, **kwargs)
    class Meta:
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"
"""
#Borra los ficheros de los platos que se eliminan.
@receiver(post_delete, sender=Dish)
def dish_delete(sender, instance, **kwargs):
    instance.dish.delete(False)
"""