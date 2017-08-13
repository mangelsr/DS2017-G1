from django.db import models
from .dish import Dish
from .lunch import Lunch

class ExcecutiveLunch(Lunch):
    dessert = models.ForeignKey(Dish, related_name="dessert")
    juice = models.ForeignKey(Dish, related_name="juice")
