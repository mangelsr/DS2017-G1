from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from catalogoapp.forms import *
from catalogoapp.models import *


def assistant_check(user):
    return user.profile.role.name == "Ayudante"


@login_required()
@user_passes_test(assistant_check, login_url='noAccess')
def listDishesAssistant(request):
    profile = request.user.profile
    restaurant = profile.restaurant
    dishes = restaurant.getDishes()
    return render(request,'listDishesAssitant.html',{"role":profile.role.name,
        "restaurant":restaurant,"dishes":dishes})


@login_required()
@user_passes_test(assistant_check, login_url='noAccess')
def listCategoryDishes(request):
    if (request.method == "POST"):
        selection = request.POST['selection']
        tipos = DishType.objects.all()
        user = request.user
        restaurant = user.profile.getRestaurant()
        dishes = Dish.objects.filter(restaurant=restaurant, dish_choice=selection)
        return render(request, 'listCategoryDishes.html', {"role":request.user.profile.role.name,
            "restaurant":restaurant,"dishes":dishes,"tipos":tipos})
    else:
        user = request.user
        restaurant = Profile.objects.get(user=user).restaurant
        tipos = DishType.objects.all()
        return render(request, 'listCategoryDishes.html', {"role":request.user.profile.role.name,
            "restaurant":restaurant,"tipos":tipos})


@login_required()
@user_passes_test(assistant_check, login_url='noAccess')
def new_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST,request.FILES)
        if form.is_valid():
            newDish = form.save(commit=False)
            newDish.restaurant = request.user.profile.restaurant
            newDish.save()
        return redirect('home')
    else:
        form = DishForm()
    return render(request,'baseform.html',{'role':request.user.profile.role.name,"form":form})


@login_required()
@user_passes_test(assistant_check, login_url='noAccess')
def edit_dish(request,id_dish):
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


@login_required()
@user_passes_test(assistant_check, login_url='noAccess')
def postLunch(request):
    if request.method == "POST":
        dish = Dish.objects.all()
        form = LunchForm(request.POST)
        form.soup.filter(restaurant=request.user.profile.restaurant)
        form.main_curse.filter(restaurant=request.user.profile.restaurant)
        if form.is_valid():
            lunch = form.save(commit=False)
            lunch.restaurant = request.user.profile.restaurant
            lunch.save()
            return redirect('home')
    else:
        form = LunchForm()
    return render(request, 'postLunch.html',{'role':request.user.profile.role.name,'lunch':form})