from django.db import models

from datetime import date

from .dish import Dish
from .restaurant import Restaurant

class Lunch(models.Model):

    BASECOST = 2.5

    soup = models.ForeignKey(Dish, related_name='soup')
    main_curse = models.ForeignKey(Dish, related_name='main_curse')
    date = models.DateField(default=date.today)
    restaurant = models.ForeignKey(Restaurant)
    stock = models.IntegerField(default=0, null=True)

    def __unicode__(self):
        return self.soup.name+" con "+self.main_curse.name

    def __str__(self):
        return self.soup.name+" con "+self.main_curse.name

    class Meta:
        verbose_name = "Lunch"
        verbose_name_plural = "Lunches"
