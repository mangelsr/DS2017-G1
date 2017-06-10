from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    url(r'^$', login, name="login"),
    url(r'^login/$', login),
    url(r'^logout/$', logout, name="logout"),

    url(r'^homeClient/$', homeClient, name='homeCliente'),
    url(r'^homeClient/listDishes$', listDishes, name='listDishes'),
    url(r'^homeClient/searchDishes$', searchDishes, name='searchDishes'),
    url(r'^homeClient/viewDish/(?P<id_dish>\d+)/$',viewDish, name='viewDish'),

    url(r'^homeAssistant/$', homeAssistant, name='homeAssistant'),
    url(r'^homeAssistant/newDish$', new_dish, name='newDish'),

    url(r'^homeAdmin/$', homeAdmin, name='homeAdmin'),
]
