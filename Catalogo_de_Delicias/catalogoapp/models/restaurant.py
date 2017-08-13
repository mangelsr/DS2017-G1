from django.db import models
from .style import Style

class Restaurant(models.Model):
    name = models.TextField(max_length=50)
    address = models.TextField()
    owner = models.TextField(max_length=50)
    phone_number = models.TextField(max_length=15)
    style = models.ForeignKey(Style)
    offer_lunch = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name

    def getDishes(self):
        from catalogoapp.models import Dish
        dishes = Dish.objects.filter(restaurant=self)
        return dishes

    def getAssistants(self):
        from catalogoapp.models import Profile
        assistants = Profile.objects.filter(restaurant=self)
        return assistants
    
    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"