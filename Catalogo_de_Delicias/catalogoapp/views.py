from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import *
from .models import *
from .forms import *

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
                return redirect('../homeAssistant')
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

def noAccess(request):
    return render(request, 'noAccess.html', {})


#VISTAS DE HOME PARA CADA ROL
def homeClient(request):
    if (request.user.is_authenticated and (request.user.profile.role == "Cliente")):
        return render(request,'homeClient.html')
    else:
        return redirect('noAccess')

def homeAssistant(request):
    if (request.user.is_authenticated and (request.user.profile.role == "Ayudante")):
        return render(request,'homeAssistant.html')
    else:
        return redirect('noAccess')

def homeAdmin(request):
    if (request.user.is_authenticated and (request.user.profile.role == "Administrador")):
        return render(request,'homeAdmin.html')
    else:
        return redirect('noAccess')

#VISTAS PARA EL ROL DE CLIENTE
def listDishes(request):
    if (request.user.is_authenticated and (request.user.profile.role == "Cliente")):
        if (request.method == "POST"):
            naperitivos = len(Dish.objects.filter(dish_choice='Aperitivo'))
            nfuertes = len(Dish.objects.filter(dish_choice='Plato Fuerte'))
            npostres = len(Dish.objects.filter(dish_choice='Postre'))
            selection = request.POST['selection']
            dishes = Dish.objects.filter(dish_choice=selection)
            ndishes = len(dishes)
            return render(request,'listDishes.html',{"ndishes":ndishes,"dishes":dishes,
            "naperitivos":naperitivos,"nfuertes":nfuertes,"npostres":npostres})
        else:
            return render(request,'listDishes.html',{})
    else:
        return redirect('noAccess')

def searchDishes(request):
    if (request.user.is_authenticated and (request.user.profile.role == "Cliente")):
        if (request.method == "POST"):
            dishName = request.POST['dishName']
            dishes = Dish.objects.filter(name__contains=dishName, description__contains=dishName)
            ndishes = len(dishes)
            return render(request,'searchDishes.html',{"ndishes":ndishes,"dishes":dishes})
        else:
            return render(request,'searchDishes.html',{})
    else:
        return redirect('noAccess')

def viewDish(request,id_dish):
    if (request.user.is_authenticated and (request.user.profile.role == "Cliente")):
        dish = Dish.objects.get(id = id_dish)
        return render(request,'detailDish.html',{"dish":dish})
    else:
        return redirect('noAccess')


#VISTAS PARA EL ROL DE AYUDANTE/ASISTENTE DE RESTAURANTE
def listDishesAssitant(request):
    if (request.user.is_authenticated and (request.user.profile.role == "Ayudante")):
        user = request.user
        restaurant = Profile.objects.get(user=user).restaurant
        dishes = Dish.objects.filter(restaurant=restaurant)
        ndishes = len(dishes)
        return render(request,'listDishesAssitant.html',{"restaurant":restaurant,"ndishes":ndishes,"dishes":dishes})
    else:
        return redirect('noAccess')

def listCategoryDishes(request):
    if (request.user.is_authenticated and (request.user.profile.role == "Ayudante")):
        if (request.method == "POST"):
            selection = request.POST['selection']
            user = request.user
            restaurant = Profile.objects.get(user=user).restaurant
            dishes = Dish.objects.filter(restaurant=restaurant, dish_choice=selection)
            ndishes = len(dishes)
            return render(request, 'listCategoryDishes.html', {"restaurant":restaurant,"ndishes":ndishes,"dishes":dishes})
        else:
            return render(request, 'listCategoryDishes.html', {})
    else:
        return redirect('noAccess')

def assistantviewDish(request,id_dish):
    if (request.user.is_authenticated and (request.user.profile.role == "Ayudante")):
        dish = Dish.objects.get(id = id_dish)
        return render(request,'detailDishAssistant.html',{"dish":dish})
    else:
        return redirect('noAccess')

def new_dish(request):
    if (request.user.is_authenticated and (request.user.profile.role == "Ayudante")):
        if request.method == 'POST':
            user = request.user
            form = DishForm(request.POST,request.FILES)
            if form.is_valid():
                newDish = form.save(commit=False)
                newDish.restaurant = Profile.objects.get(user=user).restaurant
                newDish.save()
            return redirect('homeAssistant')
        else:
            form = DishForm()
        return render(request,'dish_entry.html',{"dish":form})
    else:
        return redirect('noAccess')

def edit_dish(request,id_dish):
    if (request.user.is_authenticated and (request.user.profile.role == "Ayudante")):
        dish = Dish.objects.get(id = id_dish)
        if request.method == "GET":
            form = DishForm(instance=dish)
        else:
            form = DishForm(request.POST,request.FILES,instance=dish)
            if form.is_valid():
                newDish = form.save(commit=False)
                newDish.restaurant = Profile.objects.get(user=user).restaurant
                newDish.save()
            return redirect('homeAssistant')
        return render(request,'dish_entry.html',{"dish":form})
    else:
        return redirect('noAccess')

#VISTAS PARA EL ROL DE ADMINISTRADOR
def newRestaurant(request):
    if (request.user.is_authenticated and (request.user.profile.role == "Administrador")):
        if request.method == 'POST':
            form = RestaurantForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('homeAdmin')
        else:
            form = RestaurantForm()
        return render(request, 'newRestaurant.html',{'form': form})
    else:
        return redirect('noAccess')

def listRestaurant(request):
    if (request.user.is_authenticated and (request.user.profile.role == "Administrador")):
        restaurantes = Restaurant.objects.all()
        asistentes = Profile.objects.filter(role="Ayudante")
        platillos = Dish.objects.all()
        return render(request, 'listRestaurant.html',{'restaurantes':restaurantes,
        'asistentes':asistentes,'platillos':platillos})
    else:
        return redirect('noAccess')

def newUser(request):
    if (request.user.is_authenticated and (request.user.profile.role == "Administrador")):
        if request.method == 'POST':
            newUser = UserForm(request.POST)
            newProfile = ProfileForm(request.POST)
            if newUser.is_valid() and newProfile.is_valid():
                user = newUser.save()
                profile = newProfile.save(commit=False)
                profile.user = user
                profile.save()
            return redirect('homeAdmin')
        else:
            newUser = UserForm()
            newProfile = ProfileForm()
        return render(request,'newUser.html',{'user':newUser,'profile':newProfile})
    else:
        return redirect('noAccess')
