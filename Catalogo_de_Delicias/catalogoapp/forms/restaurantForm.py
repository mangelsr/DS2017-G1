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
            'offer_lunch',
            'style',
        ]
        labels = {
            'name': 'Nombre del restaurante',
            'address': 'Ubicacion del restaurante',
            'owner': 'Dueño del restaurante',
            'phone_number': 'Numero telefonico del restaurante',
            'offer_lunch': 'Ofrece almuerzo en linea',
            'style': 'Estilo del restaurante',
        }
        widgets = {
            'name': forms.TextInput
                (attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Nombre del restaurante aquí'}),
            'address': forms.TextInput
                (attrs={'class': 'form-control', 'id': 'address', 'placeholder': 'Ubicación del restaurante aquí'}),
            'owner': forms.TextInput
                (attrs={'class': 'form-control', 'id': 'owner', 'placeholder': 'Dueño del restaurante aquí'}),
            'phone_number': forms.TextInput
                (attrs={'class': 'form-control', 'id': 'phone_number', 'placeholder': 'Número telefónico del restaurante aquí'}),
            'offer_lunch': forms.CheckboxInput
                (attrs={'class': 'form-control', 'id': 'offer_lunch', 'placeholder': 'Seleccione si el restaurante ofrece el servicio de almuerzo en línea'}),
            'style': forms.TextInput
                (attrs={'class': 'form-control', 'id': 'style', 'placeholder': 'Estilo del restaurante aquí'}),
        }
