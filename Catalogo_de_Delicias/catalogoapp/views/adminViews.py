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
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = RestaurantForm()
    return render(request, 'baseform.html',{'role':request.user.profile.role.name,'form': form})


@login_required()
@user_passes_test(admin_check, login_url='noAccess')
def listRestaurant(request):
    restaurantes = Restaurant.objects.all()
    asistentes = Profile.objects.filter(role=2)
    platillos = Dish.objects.all()
    return render(request, 'listRestaurant.html',{'role':request.user.profile.role.name,
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
    return render(request,'newUser.html',{'role':request.user.profile.role.name,
                                          'user':newUser,'profile':newProfile})