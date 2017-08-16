from django import forms

from catalogoapp.models.lunch import Lunch
from catalogoapp.models.dish import Dish


class LunchForm(forms.ModelForm):

    class Meta:

        model = Lunch

        dishes = Dish.objects.all()
        soupChoice = []
        mainChoice = []
        for dish in dishes:
            if dish.dish_choice.name == 'Sopa':
                soupChoice.append((dish,dish.name))
            elif dish.dish_choice.name == 'Plato fuerte':
                mainChoice.append((dish,dish.name))
        print(soupChoice)
        print(mainChoice)

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
            'soup': forms.Select(attrs={'class': 'form-control', 'id': 'soup'},choices=soupChoice),
            'main_curse': forms.Select(attrs={'class': 'form-control', 'id': 'main_course'},choices=mainChoice),
            'date': forms.DateInput(),
        }