from django import forms
from django.forms.extras.widgets import SelectDateWidget

from datetime import date

from catalogoapp.models.lunch import Lunch
from catalogoapp.models.dish import Dish
from catalogoapp.models.restaurant import Restaurant
from catalogoapp.models.dishType import DishType

SOPA = DishType.objects.get(name='Sopa')
SEGUNDO = DishType.objects.get(name='Plato fuerte')


class LunchForm(forms.ModelForm):

    def __init__(self, restaurante, *args, **kwargs):
        super(LunchForm, self).__init__(*args, **kwargs)
        self.fields['soup'].queryset = restaurante.dishes_set.filter(
            dish_choice=SOPA)
        self.fields['main_curse'].queryset = restaurante.dishes_set.filter(
            dish_choice=SEGUNDO)
        self.fields['restaurant'].initial = restaurante

    date = forms.DateField(widget=forms.SelectDateWidget(), initial=date.today,
                           label='Fecha del almuerzo')
    soup = forms.ModelChoiceField(
        queryset=Dish.objects.all(), label='Sopa del almuerzo')
    main_curse = forms.ModelChoiceField(
        queryset=Dish.objects.all(), label='Plato fuerte del almuerzo')
    restaurant = forms.ModelChoiceField(
        queryset=Restaurant.objects.all(), widget=forms.HiddenInput())

    class Meta:

        model = Lunch

        fields = [
            'soup',
            'main_curse',
            'date',
            'restaurant'
        ]
