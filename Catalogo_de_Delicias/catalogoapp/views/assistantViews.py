from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from catalogoapp.forms import *
from catalogoapp.models import *


def assistant_check(user):
    return user.profile.role.name == "Ayudante"


def assistant_restaurant_check(user):
    return user.profile.role.name == "Ayudante" and user.profile.restaurant.offer_lunch


@login_required()
@user_passes_test(assistant_check, login_url='noAccess')
def listDishesAssistant(request):
    profile = request.user.profile
    restaurant = profile.restaurant
    dishes = restaurant.getDishes()
    return render(request, 'listDishesAssitant.html', {"profile": profile,
                                                       "restaurant": restaurant, "dishes": dishes})


@login_required()
@user_passes_test(assistant_check, login_url='noAccess')
def listCategoryDishes(request):
    if (request.method == "POST"):
        selection = request.POST['selection']
        tipos = DishType.objects.all()
        user = request.user
        restaurant = user.profile.getRestaurant()
        dishes = Dish.objects.filter(
            restaurant=restaurant, dish_choice=selection)
        return render(request, 'listCategoryDishes.html', {"profile": request.user.profile,
                                                           "restaurant": restaurant, "dishes": dishes, "tipos": tipos})
    else:
        user = request.user
        restaurant = Profile.objects.get(user=user).restaurant
        tipos = DishType.objects.all()
        return render(request, 'listCategoryDishes.html', {"profile": request.user.profile,
                                                           "restaurant": restaurant, "tipos": tipos})


@login_required()
@user_passes_test(assistant_check, login_url='noAccess')
def new_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            newDish = form.save(commit=False)
            newDish.restaurant = request.user.profile.restaurant
            newDish.save()
        return redirect('home')
    else:
        form = DishForm()
    return render(request, 'baseform.html', {'profile': request.user.profile, "form": form})


@login_required()
@user_passes_test(assistant_check, login_url='noAccess')
def edit_dish(request, id_dish):
    dish = Dish.objects.get(id=id_dish)
    if request.method == "GET":
        form = DishForm(instance=dish)
    else:
        form = DishForm(request.POST, request.FILES, instance=dish)
        if form.is_valid():
            newDish = form.save(commit=False)
            newDish.restaurant = request.user.profile.restaurant
            newDish.save()
        return redirect('home')
    return render(request, 'baseform.html', {'profile': request.user.profile, "form": form})


@login_required()
@user_passes_test(assistant_restaurant_check, login_url='noAccess')
def postLunch(request):
    if request.method == "POST":
        form = LunchForm(data=request.POST,
                         restaurante=request.user.profile.restaurant)
        if form.is_valid():
            form.save(commit=False)
            form.restaurant = request.user.profile.restaurant
            form.save()
            return redirect('home')
    else:
        form = LunchForm(restaurante=request.user.profile.restaurant)
    return render(request, 'postLunch.html', {'profile': request.user.profile, 'lunch': form})


@login_required()
@user_passes_test(assistant_restaurant_check, login_url='noAccess')
def postExecutiveLunch(request):
    if request.method == "POST":
        form = ExecutiveLunchForm(data=request.POST,restaurante=request.user.profile.restaurant)
        if form.is_valid():
            lunch = form.save(commit=False)
            lunch.restaurant = request.user.profile.restaurant
            lunch.save()
            return redirect('home')
    else:
        form = ExecutiveLunchForm(restaurante=request.user.profile.restaurant)
    return render(request, 'postLunch.html', {'profile': request.user.profile, 'lunch': form})
