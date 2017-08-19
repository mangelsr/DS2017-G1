from django.db import models

from .dish import Dish
from .lunch import Lunch

class ExecutiveLunch(Lunch):
    BASECOST = 3
    DESSERTCOST = 0.75
    JUICECOST = 0.5

    dessert = models.ForeignKey(Dish, related_name="dessert")
    juice = models.ForeignKey(Dish, related_name="juice")
    
    class Meta:
        verbose_name = "Executive lunch"
        verbose_name_plural = "Executive lunches"