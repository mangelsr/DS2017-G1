from django.db import models

from .profile import Profile
from .lunch import *
from .executiveLunch import *
from .schedule import Schedule
from .paymentMethod import PaymentMethod
from .creditCardMethod import CreditCardMethod
from .carnetMethod import CarnetMethod


class Order(models.Model):
    customer = models.ForeignKey(Profile)
    lunch = models.ForeignKey(Lunch)
    include_dessert = models.BooleanField()
    include_juice = models.BooleanField()
    schedule = models.ForeignKey(Schedule)
    cost = models.FloatField()
    payment = models.CharField(max_length=30)
    transaction = models.CharField(max_length=50, null=True, default="Pago realizado en efectivo")

    def __unicode__(self):
        return self.customer.user.username.capitalize()+": "+str(self.lunch)


    def __str__(self):
        return self.customer.user.username.capitalize()+": "+str(self.lunch)


    def instantiate_payment(self):
        if self.customer.is_student and self.payment == 'Carnet inteligente':
            return CarnetMethod()
        elif self.payment == 'Tarjeta de credito':
            return CreditCardMethod()


    @staticmethod
    def calculateCost(lunch, include_dessert, include_juice):
        total = lunch.BASECOST
        if hasattr(lunch, 'executivelunch'):
            total = ExecutiveLunch.BASECOST
            if include_dessert:
                total += ExecutiveLunch.DESSERTCOST
            if include_juice:
                total += ExecutiveLunch.JUICECOST
        return total


    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
