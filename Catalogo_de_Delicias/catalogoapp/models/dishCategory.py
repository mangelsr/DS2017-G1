from django.db import models

class DishCategory(models.Model):
    name = models.TextField(max_length=30)
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"