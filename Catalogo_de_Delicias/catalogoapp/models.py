from django.db import models
from django.contrib.auth.models import User
from .choices import *
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


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

class Profile(models.Model):
    role = models.CharField(max_length=20,choices=ROL,default='C',null=False,blank=False)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, related_name='profiles',null=True, blank=True, help_text='Solo necesario si el rol es Ayudante')
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
    image = models.ImageField(upload_to='photos/',null=True)
    description = models.TextField()
    dish_choice = models.CharField(max_length=20,choices=DISH_CHOICE,default='A',null=False,blank=False)
    temperature = models.CharField(max_length=20,choices=TEMPERATURE,default='C',null=False,blank=False)
    restaurant = models.ForeignKey(Restaurant,related_name='dishes')
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
    """
    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Dish, self).delete(*args, **kwargs)
    """
    class Meta:
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"

#Borra los ficheros de los platos que se eliminan.
@receiver(pre_delete, sender=Dish)
def dish_delete(sender, instance, **kwargs):
    instance.dish.delete(False)
