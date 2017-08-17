from django.db import models
from .dish import Dish
from .restaurant import Restaurant

class Lunch(models.Model):
    soup = models.ForeignKey(Dish, related_name='soup')
    main_curse = models.ForeignKey(Dish, related_name='main_curse')
    date = models.DateField()
    restaurant = models.ForeignKey(Restaurant)

    def __unicode__(self):
        return self.soup.name+" con "+self.main_curse.name

    def __str__(self):
        return self.soup.name+" con "+self.main_curse.name

    class Meta:
        verbose_name = "Lunch"
        verbose_name_plural = "Lunches"
