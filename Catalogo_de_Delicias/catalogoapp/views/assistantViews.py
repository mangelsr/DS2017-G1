from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from catalogoapp.forms import *
from catalogoapp.models import *


@login_required(login_url='login')
def listDishesAssistant(request):
    if (request.user.profile.role.name == "Ayudante"):
        profile = request.user.profile
        restaurant = profile.restaurant
        dishes = restaurant.getDishes()
        return render(request,'listDishesAssitant.html',{"role":profile.role.name,
            "restaurant":restaurant,"dishes":dishes})
    else:
        return redirect('noAccess')


@login_required(login_url='login')
def listCategoryDishes(request):
    if (request.user.profile.role.name == "Ayudante"):
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
    else:
        return redirect('noAccess')


@login_required(login_url='login')
def new_dish(request):
    if (request.user.profile.role.name == "Ayudante"):
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


@login_required(login_url='login')
def edit_dish(request,id_dish):
    if (request.user.profile.role.name == "Ayudante"):
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


@login_required(login_url='login')
def postLunch(request):
    return render(request, 'postLunch.html')