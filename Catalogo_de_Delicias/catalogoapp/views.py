from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from .models import *

# Create your views here.

def login(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            rol = Profile.objects.get(user=user).role
            if (rol=="Cliente"):
                return redirect('../homeClient')
            elif (rol=="Ayudante"):
                return redirect('../homeAsistant')
            else:
                return redirect('../homeAdmin')
        else:
            print("ERROR DE AUTENTICACION...")
            return render(request,'login.html',{'error':True})
    else:
        return render(request,'login.html',{})

def logout(request):
    auth_logout(request)
    return render(request,'logout.html',{})

def homeClient(request):
    if request.user.is_authenticated:
        return render(request,'homeClient.html')
    else:
        print("DEBE ESTAR LOGEADO...")
        return redirect('../')

def listDishes(request):
    if (request.method == "POST"):
        selection = request.POST['selection']
        dishes = Dish.objects.filter(dish_choice=selection)
        ndishes = len(dishes)
        return render(request,'listDishes.html',{"ndishes":ndishes,"dishes":dishes})
    else:
        return render(request,'listDishes.html',{})

def searchDish(request):
    if (request.method == "POST"):
        dishName = request.POST['dishName']
        dishes = Dish.objects.filter(name__contains=dishName)
        ndishes = len(dishes)
        return render(request,'searchDish.html',{"ndishes":ndishes,"dishes":dishes})
    else:
        return render(request,'searchDish.html',{})
