from django.shortcuts import render, redirect
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from catalogoapp.models import *


@login_required(login_url='login')
def listDishesClient(request):
    if (request.user.profile.role.name == "Cliente"):
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
    else:
        return redirect('noAccess')


@login_required(login_url='login')
def searchDishes(request):
    if (request.user.profile.role.name == "Cliente"):
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
    else:
        return redirect('noAccess')


@login_required(login_url='login')
def viewDish(request,id_dish):
    if (request.user.profile.role.name == "Cliente" or request.user.profile.role.name == "Ayudante"):
        dish = Dish.objects.get(id = id_dish)
        return render(request, 'detailDish.html', {'role': request.user.profile.role.name, "dish": dish})
    else:
        return redirect('noAccess')


@login_required(login_url='login')
def orderLunch(request):
    return render(request, 'orderLunch.html')
