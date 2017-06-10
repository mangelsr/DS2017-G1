from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
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
    url(r'^homeAssistant/listDishes$', listDishesAssitant, name='listDishesAssitant'),
    url(r'^homeAssistant/listCategoryDishes$', listCategoryDishes, name='listCategoryDishes'),
    url(r'^homeAssistant/newDish$', new_dish, name='newDish'),
    url(r'^homeAssistant/viewDish/(?P<id_dish>\d+)/$',assistantviewDish, name='assistantviewDish'),

    url(r'^homeAdmin/$', homeAdmin, name='homeAdmin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
