from django import forms

from catalogoapp.models.lunch import Lunch
from catalogoapp.models.dish import Dish


class LunchForm(forms.ModelForm):

    class Meta:

        model = Lunch
        """
        dishes = Dish.objects.all()
        soupChoice = []
        mainChoice = []
        for dish in dishes:
            if dish.dish_choice.name == 'Sopa' and dish.restaurant == model.restaurant:
                soupChoice.append((dish.name, dish.name))
            elif dish.dish_choice.name == 'Plato fuerte' and dish.restaurant == model.restaurant:
                mainChoice.append((dish.name, dish.name))
        """
        fields = [
            'soup',
            'main_curse',
            'date',
        ]
        labels = {
            'soup': 'Sopa del almuerzo',
            'main_curse': 'Plato fuerte del almuerzo',
            'date': 'Fecha del almuerzo',
        }
        widgets = {
            'soup': forms.Select(attrs={'class': 'form-control', 'id': 'soup'}),
            'main_curse': forms.Select(attrs={'class': 'form-control', 'id': 'main_course'}),
            'date': forms.DateInput()
        }