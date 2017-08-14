from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        labels = {
            'username': 'Nombre de Usuario',
            'password': 'Contraseña',
        }
        widgets = {
            'title': forms.TextInput
                (attrs={'class': 'form-control', 'id': 'username', 'placeholder': 'Su nombre de usuario aqui'}),
            'password': forms.PasswordInput
                (attrs={'class': 'form-control', 'id': 'password', 'placeholder': 'Su contraseña aqui'}),
        }
