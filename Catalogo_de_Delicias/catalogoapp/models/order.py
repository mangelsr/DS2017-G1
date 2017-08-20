from django.db import models

from .profile import Profile
from .lunch import *
from .executiveLunch import *
from .schedule import Schedule


class Order(models.Model):
    customer = models.ForeignKey(Profile)
    lunch = models.ForeignKey(Lunch)
    include_dessert = models.BooleanField()
    include_juice = models.BooleanField()
    schedule = models.ForeignKey(Schedule)
    cost = models.FloatField()

    def __unicode__(self):
        return self.customer.user.username.capitalize()+": "+str(self.lunch)


    def __str__(self):
        return self.customer.user.username.capitalize()+": "+str(self.lunch)


    @staticmethod
    def calculateCost(lunch, include_dessert, include_juice):
        total = BASECOST
        if hasattr(lunch, 'executivelunch'):
            if include_dessert:
                total += DESSERTCOST
            if include_juice:
                total += JUICECOST
        return total


    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
