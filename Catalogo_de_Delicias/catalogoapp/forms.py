from django.contrib.auth.models import User
from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
        labels = {
            'username' : 'Nombre de Usuario',
            'password' : 'Contraseña'
        }
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','id':'username','placeholder':'Su nombre de usuario aqui'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control','id':'password','placeholder':'Su contraseña aqui'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'role'
        ]
        labels = {
            'role' : 'Rol del usuario'
        }
        widgets = {
            'role' : forms.Select()
        }

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'address',
            'owner',
            'phone_number'
        ]
        labels = {
            'name' : 'Nombre del restaurante',
            'address' : 'Ubicacion del restaurante',
            'owner' : 'Dueño del restaurante',
            'phone_number' : 'Numero telefonico del restaurante'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','id':'name','placeholder':'Nombre del restaurante aqui'}),
            'address' : forms.TextInput(attrs={'class':'form-control','id':'address','placeholder':'Ubicacion del restaurante aqui'}),
            'owner' : forms.TextInput(attrs={'class':'form-control','id':'owner','placeholder':'Dueño del restaurante aqui'}),
            'phone_number' : forms.TextInput(attrs={'class':'form-control','id':'phone_number','placeholder':'Numero telefonico del restaurante aqui'})
        }

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = [
            'name',
            'ingredients',
            #'image',
            'description',
            'dish_choice',
            'temperature'
        ]
        labels = {
            'name' : 'Nombre del plato',
            'ingredients' : 'Ingredientes del plato',
            #'image' : 'Imagen del plato',
            'description' : 'Descripcion del plato',
            'dish_choice' : 'Tipo de plato',
            'temperature' : 'Temperatura del plato'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','id':'name','placeholder':'Nombre del plato aqui'}),
            'ingredients' : forms.TextInput(attrs={'class':'form-control','id':'ingredients','placeholder':'Ingredientes del plato aqui'}),
            #'image' : forms.FileInput(),
            'description' : forms.TextInput(attrs={'class':'form-control','id':'description','placeholder':'Descripcion del plato aqui'}),
            'dish_choice' : forms.Select(),
            'temperature' : forms.Select()
        }
