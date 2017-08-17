from django import forms
from django.forms.extras.widgets import SelectDateWidget

from catalogoapp.models.lunch import Lunch
from catalogoapp.models.dish import Dish
from catalogoapp.models.restaurant import Restaurant
from catalogoapp.models.dishType import DishType

SOPA = DishType.objects.get(name='Sopa')


class LunchForm(forms.ModelForm):

    def __init__(self, restaurante, *args, **kwargs):
        super(LunchForm, self).__init__(*args, **kwargs)
        self.fields['soup'].queryset = restaurante.dishes_set.filter(
            dish_choice=SOPA)
        self.fields['restaurant'].initial = restaurante

    date = forms.DateField(widget=forms.SelectDateWidget(),
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
