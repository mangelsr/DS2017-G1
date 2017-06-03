from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from .models import Perfil

# Create your views here.

def login(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            rol = Perfil.objects.get(user=user).rol
            return redirect('../home')
        else:
            print("ERROR DE AUTENTICACION...")
            return render(request,'login.html',{'error':True})
    else:
        return render(request,'login.html',{})

def logout(request):
    auth_logout(request)
    return render(request,'logout.html',{})

def home(request):
    if request.user.is_authenticated:
        user = request.user
        rol = Perfil.objects.get(user=user).rol
        return render(request,'home.html',{"rol":rol})
    else:
        print("DEBE ESTAR LOGEADO...")
        return redirect('../')
