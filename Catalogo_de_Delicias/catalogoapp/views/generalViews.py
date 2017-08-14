from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


def login(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            print("ERROR DE AUTENTICACION...")
            return render(request,'login.html', {'error':True})
    else:
        return render(request, 'login.html', {})


def logout(request):
    auth_logout(request)
    return render(request, 'logout.html', {})


def noAccess(request):
    return render(request, 'noAccess.html', {})


@login_required(login_url='login')
def home(request):
    role = request.user.profile.role.name
    return render(request, 'home.html', {'role': role})
