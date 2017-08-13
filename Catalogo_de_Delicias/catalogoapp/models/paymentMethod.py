from django.db import models

class PaymentMethod(models.Model):
    name = models.TextField(max_length=50)

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Payment Method"
        verbose_name_plural = "Payment Methods"