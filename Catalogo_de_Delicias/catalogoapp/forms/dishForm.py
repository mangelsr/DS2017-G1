from django import forms

from catalogoapp.models.dish import Dish


class DishForm(forms.ModelForm):

    class Meta:
        model = Dish
        fields = [
            'name',
            'ingredients',
            'image',
            'description',
            'dish_choice',
            'dish_category',
            'temperature',
        ]
        labels = {
            'name': 'Nombre del plato',
            'ingredients': 'Ingredientes del plato',
            'image': 'Imagen del plato',
            'description': 'Descripcion del plato',
            'dish_choice': 'Tipo de plato',
            'dish_category': 'Categoria del plato',
            'temperature': 'Temperatura del plato',
        }
        widgets = {
            'name': forms.TextInput
                (attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Nombre del plato aqui'}),
            'ingredients': forms.TextInput
                (attrs={'class': 'form-control', 'id': 'ingredients', 'placeholder': 'Ingredientes del plato aqui'}),
            'image': forms.FileInput(),
            'description': forms.TextInput
                (attrs={'class': 'form-control', 'id': 'description', 'placeholder': 'Descripcion del plato aqui'}),
            'dish_choice': forms.Select(),
            'dish_category': forms.Select(),
            'temperature': forms.Select(),
        }
