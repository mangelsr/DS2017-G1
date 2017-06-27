from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(DishType)
admin.site.register(DishTemperature)
admin.site.register(DishCategory)
