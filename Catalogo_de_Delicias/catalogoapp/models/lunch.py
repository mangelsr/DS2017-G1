from django.db import models
from .dish import Dish

class Lunch(models.Model):
    soup = models.ForeignKey(Dish, related_name="soup")
    main_curse = models.ForeignKey(Dish, related_name="main_curse")
    date = models.DateField()
    
    class Meta:
        verbose_name = "Lunch"
        verbose_name_plural = "Lunches"
