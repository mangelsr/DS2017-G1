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
            if (rol == 'Cliente'):
                return redirect('../homeCliente')
            elif (rol == 'Ayudante'):
                return redirect('../homeAyudante')
            else:
                return redirect('../homeAdmin')
        else:
            print("ERROR DE AUTENTICACION...")
            response = HttpResponse("ERROR DE AUTENTICACION...",status=500)
            return response
    else:
        return render(request,'login.html',{})

def logout(request):
    auth_logout(request)
    return render(request,'logout.html',{})
