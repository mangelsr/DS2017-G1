from django.db import models
from .profile import Profile
from .lunch import Lunch
from .paymentMethod import PaymentMethod

class Order(models.Model):
    customer = models.ForeignKey(Profile)
    lunch = models.ForeignKey(Lunch)
    include_dessert = models.BooleanField()
    include_juice = models.BooleanField()
    cost = models.FloatField()
    paymentMethod = models.ForeignKey(PaymentMethod)
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"