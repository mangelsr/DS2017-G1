from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from .views import *

from . import views
urlpatterns = [
    url(r'^$', login),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
]
