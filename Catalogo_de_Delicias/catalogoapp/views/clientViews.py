from django.shortcuts import render, redirect
from django.db.models import Count
from django.contrib.auth.decorators import login_required, user_passes_test
import datetime
from catalogoapp.models import *


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
        return render(request, 'listDishesClient.html', {'role': request.user.profile.role.name,
                                                         'tipos': tipos, 'cuentaTipos': cuentaTipos})
    elif (request.method == "POST"):
        selection = request.POST['selection']
        dishes = Dish.objects.filter(dish_choice=selection)
        cuentaTipos = DishType.objects.annotate(nTypes=Count('dish'))
        tipos = DishType.objects.all()
        return render(request, 'listDishesClient.html', {'role': request.user.profile.role.name,
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
        return render(request, 'searchDishes.html', {'role': request.user.profile.role.name, "dishes": dishes})
    else:
        return render(request, 'searchDishes.html', {'role': request.user.profile.role.name})


@login_required()
@user_passes_test(user_assistant_check, login_url='noAccess')
def viewDish(request,id_dish):
    if (request.user.profile.role.name == "Cliente" or request.user.profile.role.name == "Ayudante"):
        dish = Dish.objects.get(id = id_dish)
        return render(request, 'detailDish.html', {'role': request.user.profile.role.name, "dish": dish})
    else:
        return redirect('noAccess')


@login_required()
@user_passes_test(user_check, login_url='noAccess')
def orderLunch(request):
    restaurants = Restaurant.objects.filter(offer_lunch=True)
    return render(request, 'orderLunch.html', {'role': request.user.profile.role.name,
                                               'restaurants': restaurants})

@login_required()
@user_passes_test(user_check, login_url='noAccess')
def selectLunch(request, id_restaurant):
    lunches = Lunch.objects.filter(restaurant=id_restaurant, date=datetime.date.today())
    executiveLunches = ExcecutiveLunch.objects.filter(restaurant=id_restaurant, date=datetime.date.today())
    return render(request, 'selectLunch.html', {'role': request.user.profile.role.name, 'lunches': lunches,
                                                'executives': executiveLunches})