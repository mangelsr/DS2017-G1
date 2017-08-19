from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from catalogoapp.forms import *
from catalogoapp.models import *


def admin_check(user):
    return user.profile.role.name == "Administrador"


@login_required()
@user_passes_test(admin_check, login_url='noAccess')
def newRestaurant(request):
    if request.method == 'POST':
        restaurantform = RestaurantForm(request.POST)
        styleform = StyleForm(request.POST)
        if restaurantform.is_valid():
            newStyle = styleform.save()
            newRestaurant = restaurantform.save(commit=False)
            newRestaurant.style = newStyle
            newRestaurant.save()
        return redirect('home')
    else:
        restaurantform = RestaurantForm()
        styleform = StyleForm()
    return render(request, 'baseform2.html',{'profile':request.user.profile,'form1': restaurantform,'form2': styleform})


@login_required()
@user_passes_test(admin_check, login_url='noAccess')
def listRestaurant(request):
    restaurantes = Restaurant.objects.all()
    asistentes = Profile.objects.filter(role=2)
    platillos = Dish.objects.all()
    return render(request, 'listRestaurant.html',{'profile':request.user.profile,
                                                  'restaurantes':restaurantes,
                                                  'asistentes':asistentes,'platillos':platillos})


@login_required()
@user_passes_test(admin_check, login_url='noAccess')
def newUser(request):
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
    return render(request,'baseform2.html',{'profile':request.user.profile,
                                          'form1':newUser,'form2':newProfile})