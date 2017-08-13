from django.db import models
from .restaurant import Restaurant
from .dishCategory import DishCategory
from .dishTemperature import DishTemperature
from .dishType import DishType

class Dish(models.Model):
    name = models.TextField(max_length=50)
    ingredients = models.TextField()
    image = models.ImageField(upload_to='photos/', null=True)
    description = models.TextField()
    dish_choice = models.ForeignKey(DishType)
    dish_category = models.ForeignKey(DishCategory, null=True)
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
