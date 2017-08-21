from django.shortcuts import render, redirect
from django.db.models import Count
from django.contrib.auth.decorators import login_required, user_passes_test

import datetime

from catalogoapp.models import *
from catalogoapp.forms import OrderForm


def user_check(user):
    return user.profile.role.name == "Cliente"


def user_assistant_check(user):
    return user.profile.role.name == "Cliente" or user.profile.role.name == "Ayudante"


@login_required()
@user_passes_test(user_check, login_url='noAccess')
def listDishesClient(request):
    if request.method == "GET":
        cuentaTipos = DishType.objects.annotate(nTypes=Count('dish'))
        tipos = DishType.objects.all()
        return render(request, 'listDishesClient.html', {'profile': request.user.profile,
                                                         'tipos': tipos, 'cuentaTipos': cuentaTipos})
    elif (request.method == "POST"):
        selection = request.POST['selection']
        dishes = Dish.objects.filter(dish_choice=selection)
        cuentaTipos = DishType.objects.annotate(nTypes=Count('dish'))
        tipos = DishType.objects.all()
        return render(request, 'listDishesClient.html', {'profile': request.user.profile,
                                                         'tipos': tipos, 'cuentaTipos': cuentaTipos,
                                                         'dishes': dishes})


@login_required()
@user_passes_test(user_check, login_url='noAccess')
def searchDishes(request):
    if (request.method == "POST"):
        dishName = request.POST['dishName']
        name_dishes = Dish.objects.filter(name__contains=dishName)
        description_dishes = Dish.objects.filter(description__contains=dishName)
        dishes = list(name_dishes)
        for dish in description_dishes:
            if dish not in dishes:
                dishes.append(dish)
        return render(request, 'searchDishes.html', {'profile': request.user.profile, "dishes": dishes})
    else:
        return render(request, 'searchDishes.html', {'profile': request.user.profile})


@login_required()
@user_passes_test(user_assistant_check, login_url='noAccess')
def viewDish(request,id_dish):
    dish = Dish.objects.get(id = id_dish)
    return render(request, 'detailDish.html', {'profile': request.user.profile, "dish": dish})


@login_required()
@user_passes_test(user_check, login_url='noAccess')
def orderLunch(request):
    restaurants = Restaurant.objects.filter(offer_lunch=True)
    return render(request, 'orderLunch.html', {'profile': request.user.profile,
                                               'restaurants': restaurants})


@login_required()
@user_passes_test(user_check, login_url='noAccess')
def selectLunch(request, id_restaurant):
    lunches = Lunch.objects.filter(restaurant=id_restaurant, date=datetime.date.today())
    executiveLunches = ExecutiveLunch.objects.filter(restaurant=id_restaurant,
                                                    date=datetime.date.today())
    restaurant = Restaurant.objects.get(id=id_restaurant)
    normalLunches = [l for l in lunches if not hasattr(l, 'executivelunch')]
    return render(request, 'selectLunch.html', {'profile': request.user.profile, 
                                                'lunches': normalLunches,
                                                'executives': executiveLunches,
                                                'restaurant': restaurant})


@login_required()
@user_passes_test(user_check, login_url='noAccess')
def payLunch(request, id_lunch):
    lunch = Lunch.objects.filter(id=id_lunch)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user.profile
            order.lunch = lunch[0]
            order.cost = Order.calculateCost(lunch[0], order.include_dessert, order.include_juice)
            try:
                order.transaction = order.instantiate_payment().pagar(order.cost, True)
            except:
                pass
            order.save()
        return redirect('home')
    else:
        form = OrderForm()
    return render(request, 'payLunch.html', {'profile': request.user.profile, 'form': form})
