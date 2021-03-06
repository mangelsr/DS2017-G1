from django.db import models

class DishTemperature(models.Model):
    name = models.TextField(max_length=25)
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Temperature"
        verbose_name_plural = "Temperatures"