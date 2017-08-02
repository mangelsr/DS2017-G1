from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.db.models import Count
from .forms import *
from .models import *

# Create your views here.

def login(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            print("ERROR DE AUTENTICACION...")
            return render(request,'login.html', {'error':True})
    else:
        return render(request, 'login.html', {})

def logout(request):
    auth_logout(request)
    return render(request,'logout.html',{})

def noAccess(request):
    return render(request, 'noAccess.html', {})

def home(request):
    if (request.user.is_authenticated):
        role = request.user.profile.role.name
        return render(request,'home.html',{'role':role})
    else:
        return redirect('noAccess')

#VISTAS PARA EL ROL DE CLIENTE
def listDishesClient(request):
    if (request.user.is_authenticated and request.user.profile.role.name == "Cliente"):
        if request.method == "GET":
            cuentaTipos = DishType.objects.annotate(nTypes=Count('dish'))
            tipos = DishType.objects.all()
            return render(request,'listDishesClient.html',{'role':request.user.profile.role.name,'tipos':tipos,
            'cuentaTipos':cuentaTipos})
        elif (request.method == "POST"):   
            selection = request.POST['selection']
            dishes = Dish.objects.filter(dish_choice=selection)
            cuentaTipos = DishType.objects.annotate(nTypes=Count('dish'))
            tipos = DishType.objects.all()
            return render(request,'listDishesClient.html',{'role':request.user.profile.role.name,'tipos':tipos,
            'cuentaTipos':cuentaTipos,'dishes':dishes})
    else:
        return redirect('noAccess')

def searchDishes(request):
    if (request.user.is_authenticated and (request.user.profile.role.name == "Cliente"
        or request.user.profile.role.name == "Ayudante")):
        if (request.method == "POST"):
            dishName = request.POST['dishName']
            name_dishes = Dish.objects.filter(name__contains=dishName)
            description_dishes = Dish.objects.filter(description__contains=dishName)
            dishes = list(name_dishes)
            for dish in description_dishes:
                if dish not in dishes:
                    dishes.append(dish)
            return render(request,'searchDishes.html',{'role':request.user.profile.role.name,"dishes":dishes})
        else:
            return render(request,'searchDishes.html',{'role':request.user.profile.role.name,})
    else:
        return redirect('noAccess')

def viewDish(request,id_dish):
    if (request.user.is_authenticated and (request.user.profile.role.name == "Cliente"
        or request.user.profile.role.name == "Ayudante")):
        dish = Dish.objects.get(id = id_dish)
        return render(request,'detailDish.html',{'role':request.user.profile.role.name,"dish":dish})
    else:
        return redirect('noAccess')


#VISTAS PARA EL ROL DE AYUDANTE/ASISTENTE DE RESTAURANTE
def listDishesAssistant(request):
    if (request.user.is_authenticated and (request.user.profile.role.name == "Ayudante")):
        if (request.method == "POST"):
            selection = request.POST['selection']
            user = request.user
            restaurant = Profile.objects.get(user=user).restaurant
            dishes = Dish.objects.filter(restaurant=restaurant, dish_choice=selection)
            ndishes = len(dishes)
            return render(request, 'listDishesAssistant.html', {"restaurant":restaurant,"ndishes":ndishes,"dishes":dishes})
        else:
            return render(request, 'listDishesAssistant.html', {})
    else:
        return redirect('noAccess')

def listCategoryDishes(request):
    if (request.user.is_authenticated and (request.user.profile.role.name == "Ayudante")):
        if (request.method == "POST"):
            selection = request.POST['selection']
            user = request.user
            restaurant = Profile.objects.get(user=user).restaurant
            dishes = Dish.objects.filter(restaurant=restaurant, dish_choice=selection)
            ndishes = len(dishes)
            return render(request, 'listDishesAssistant.html', {"restaurant":restaurant,"ndishes":ndishes,"dishes":dishes})
        else:
            return render(request, 'listDishesAssistant.html', {})
    else:
        return redirect('noAccess')

def new_dish(request):
    if (request.user.is_authenticated and (request.user.profile.role.name == "Ayudante")):
        if request.method == 'POST':
            user = request.user
            form = DishForm(request.POST,request.FILES)
            if form.is_valid():
                newDish = form.save(commit=False)
                newDish.restaurant = user.profile.restaurant
                newDish.save()
            return redirect('home')
        else:
            form = DishForm()
        return render(request,'baseform.html',{'role':request.user.profile.role.name,"form":form})
    else:
        return redirect('noAccess')

def edit_dish(request,id_dish):
    if (request.user.is_authenticated and (request.user.profile.role.name == "Ayudante")):
        dish = Dish.objects.get(id = id_dish)
        if request.method == "GET":
            form = DishForm(instance=dish)
        else:
            form = DishForm(request.POST,request.FILES,instance=dish)
            if form.is_valid():
                newDish = form.save(commit=False)
                newDish.restaurant = request.user.profile.restaurant
                newDish.save()
            return redirect('home')
        return render(request,'baseform.html',{'role':request.user.profile.role.name,"form":form})
    else:
        return redirect('noAccess')

#VISTAS PARA EL ROL DE ADMINISTRADOR
def newRestaurant(request):
    if (request.user.is_authenticated and (request.user.profile.role.name == "Administrador")):
        if request.method == 'POST':
            form = RestaurantForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('home')
        else:
            form = RestaurantForm()
        return render(request, 'baseform.html',{'role':request.user.profile.role.name,'form': form})
    else:
        return redirect('noAccess')

def listRestaurant(request):
    if (request.user.is_authenticated and (request.user.profile.role.name == "Administrador")):
        restaurantes = Restaurant.objects.all()
        asistentes = Profile.objects.filter(role=2)
        platillos = Dish.objects.all()
        return render(request, 'listRestaurant.html',{'role':request.user.profile.role.name,'restaurantes':restaurantes,
        'asistentes':asistentes,'platillos':platillos})
    else:
        return redirect('noAccess')

def newUser(request):
    if (request.user.is_authenticated and (request.user.profile.role.name == "Administrador")):
        if request.method == 'POST':
            newUser = UserForm(request.POST)
            newProfile = ProfileForm(request.POST)
            if newUser.is_valid() and newProfile.is_valid():
                user = newUser.save()
                user.set_password(user.password)
                user.save()
                profile = newProfile.save(commit=False)
                profile.user = user
                profile.save()
            return redirect('home')
        else:
            newUser = UserForm()
            newProfile = ProfileForm()
        return render(request,'newUser.html',{'role':request.user.profile.role.name,'user':newUser,'profile':newProfile})
    else:
        return redirect('noAccess')
