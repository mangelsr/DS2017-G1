from django import forms
from catalogoapp.models.restaurant import Restaurant


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'address',
            'owner',
            'phone_number',
        ]
        labels = {
            'name': 'Nombre del restaurante',
            'address': 'Ubicacion del restaurante',
            'owner': 'Dueño del restaurante',
            'phone_number': 'Numero telefonico del restaurante',
        }
        widgets = {
            'name': forms.TextInput
                (attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Nombre del restaurante aqui'}),
            'address': forms.TextInput
                (attrs={'class': 'form-control', 'id': 'address', 'placeholder': 'Ubicacion del restaurante aqui'}),
            'owner': forms.TextInput
                (attrs={'class': 'form-control', 'id': 'owner', 'placeholder': 'Dueño del restaurante aqui'}),
            'phone_number': forms.TextInput
                (attrs={'class': 'form-control', 'id': 'phone_number', 'placeholder': 'Numero telefonico del restaurante aqui'}),
        }
