from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    #URLS DE INCIO/CIERRE/PERMISOS
    url(r'^$', login, name="login"),
    url(r'^login/$', login),
    url(r'^logout/$', logout, name="logout"),
    url(r'^noAccess/$', noAccess, name="noAccess"),

    url(r'^home/$', home, name="home"),

    #URLS DEL ROL CLIENTE
    url(r'^home/listDishesClient$', listDishesClient, name="listDishesClient"),
    url(r'^home/searchDishes$', searchDishes, name="searchDishes"),
    url(r'^home/viewDish/(?P<id_dish>\d+)/$',viewDish, name="viewDish"),

    #URLS DEL ROL AYUDANTE/ASISTENTE
    url(r'^home/newDish$', new_dish, name="newDish"),    
    url(r'^home/listDishesAssistant$', listDishesAssistant, name="listDishesAssistant"),
    url(r'^home/listCategoryDishes$', listCategoryDishes, name="listCategoryDishes"),
    url(r'^home/editDish/(?P<id_dish>\d+)/$',edit_dish, name="editDish"),

    #URLS DEL ROL ADMINISTRADOR
    url(r'^home/newRestaurant$', newRestaurant, name="newRestaurant"),
    url(r'^home/listRestaurant$', listRestaurant, name="listRestaurant"),
    url(r'^home/newUser$', newUser, name="newUser"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
