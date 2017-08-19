from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    #URLS DE INCIO/CIERRE/PERMISOS
    url(r'^$', home, name="home"),
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^noAccess/$', noAccess, name="noAccess"),

    #URLS DEL ROL CLIENTE
    url(r'^listDishesClient$', listDishesClient, name="listDishesClient"),
    url(r'^searchDishes$', searchDishes, name="searchDishes"),
    url(r'^viewDish/(?P<id_dish>\d+)/$', viewDish, name="viewDish"),
    url(r'^orderLunch$', orderLunch, name="orderLunch"),
    url(r'^selectLunch/(?P<id_restaurant>\d+)/$', selectLunch, name="selectLunch"),
    url(r'^payLunch/(?P<id_lunch>\d+)/$', payLunch, name="payLunch"),

    #URLS DEL ROL AYUDANTE/ASISTENTE
    url(r'^newDish$', new_dish, name="newDish"),    
    url(r'^listDishesAssistant$', listDishesAssistant, name="listDishesAssistant"),
    url(r'^listCategoryDishes$', listCategoryDishes, name="listCategoryDishes"),
    url(r'^editDish/(?P<id_dish>\d+)/$', edit_dish, name="editDish"),
    url(r'^postLunch$', postLunch, name="postLunch"),
    url(r'^postExecutiveLunch$', postExecutiveLunch, name="postExecutiveLunch"),

    #URLS DEL ROL ADMINISTRADOR
    url(r'^newRestaurant$', newRestaurant, name="newRestaurant"),
    url(r'^listRestaurant$', listRestaurant, name="listRestaurant"),
    url(r'^newUser$', newUser, name="newUser"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
