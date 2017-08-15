from django.db import models
from django.contrib.auth.models import User
from .role import Role
from .restaurant import Restaurant


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='profile', on_delete=models.CASCADE)
    role = models.ForeignKey(Role, null=False, blank=False)
    restaurant = models.ForeignKey(Restaurant, related_name='restaurant', null=True, blank=True, help_text='Solo necesario si el rol es Ayudante')
    is_student = models.BooleanField()
    
    def __unicode__(self):
        return self.user.username
    
    def __str__(self):
        return self.user.username
    
    def getRestaurant(self):
        return self.restaurant
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
