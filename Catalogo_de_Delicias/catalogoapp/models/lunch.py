from django.db import models
from .dish import Dish
from .restaurant import Restaurant

class Lunch(models.Model):
    soup = models.ForeignKey(Dish, related_name='soup')
    main_curse = models.ForeignKey(Dish, related_name='main_curse')
    date = models.DateField()
    restaurant = models.ForeignKey(Restaurant)

    class Meta:
        verbose_name = "Lunch"
        verbose_name_plural = "Lunches"
