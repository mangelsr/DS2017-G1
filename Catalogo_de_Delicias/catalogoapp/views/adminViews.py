from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from catalogoapp.forms import *
from catalogoapp.models import *

@login_required(login_url='login')
def newRestaurant(request):
    if (request.user.profile.role.name == "Administrador"):
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


@login_required(login_url='login')
def listRestaurant(request):
    if (request.user.profile.role.name == "Administrador"):
        restaurantes = Restaurant.objects.all()
        asistentes = Profile.objects.filter(role=2)
        platillos = Dish.objects.all()
        return render(request, 'listRestaurant.html',{'role':request.user.profile.role.name,'restaurantes':restaurantes,
        'asistentes':asistentes,'platillos':platillos})
    else:
        return redirect('noAccess')


@login_required(login_url='login')
def newUser(request):
    if (request.user.profile.role.name == "Administrador"):
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