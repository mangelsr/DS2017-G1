from django.db import models

class DishType(models.Model):
    name = models.CharField(max_length=25)
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"
