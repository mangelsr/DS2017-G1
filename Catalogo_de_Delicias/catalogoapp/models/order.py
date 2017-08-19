from django.db import models
from .profile import Profile
from .lunch import Lunch
from .schedule import Schedule


class Order(models.Model):
    customer = models.ForeignKey(Profile)
    lunch = models.ForeignKey(Lunch)
    include_dessert = models.BooleanField()
    include_juice = models.BooleanField()
    schedule = models.ForeignKey(Schedule)
    cost = models.FloatField()

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
