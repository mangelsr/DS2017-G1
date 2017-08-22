from django import forms

from datetime import date

from catalogoapp.models.executiveLunch import ExecutiveLunch
from catalogoapp.models.dish import Dish
from catalogoapp.models.restaurant import Restaurant
from catalogoapp.models.dishType import DishType

SOPA = DishType.objects.get(name='Sopa')
SEGUNDO = DishType.objects.get(name='Plato fuerte')
JUGO = DishType.objects.get(name='Jugo')
POSTRE = DishType.objects.get(name='Postre')

class ExecutiveLunchForm(forms.ModelForm):

    def __init__(self, restaurante, *args, **kwargs):
        super(ExecutiveLunchForm, self).__init__(*args, **kwargs)
        self.fields['soup'].queryset = restaurante.dishes_set.filter(
            dish_choice=SOPA)
        self.fields['main_curse'].queryset = restaurante.dishes_set.filter(
            dish_choice=SEGUNDO)
        self.fields['juice'].queryset = restaurante.dishes_set.filter(
            dish_choice=JUGO)
        self.fields['dessert'].queryset = restaurante.dishes_set.filter(
            dish_choice=POSTRE)
        self.fields['restaurant'].initial = restaurante

    date = forms.DateField(widget = forms.SelectDateWidget(), initial=date.today, label='Fecha del almuerzo')
    soup = forms.ModelChoiceField(queryset=Dish.objects.all(), label='Sopa del almuerzo')
    main_curse = forms.ModelChoiceField(queryset=Dish.objects.all(), label='Plato fuerte del almuerzo')
    juice = forms.ModelChoiceField(queryset=Dish.objects.all(), label='Jugo del almuerzo')
    dessert = forms.ModelChoiceField(queryset=Dish.objects.all(),label='Postre del almuerzo')
    stock = forms.IntegerField(min_value=1, label='Cantidad de almuerzos')
    restaurant = forms.ModelChoiceField(
        queryset=Restaurant.objects.all(), widget=forms.HiddenInput())  

    class Meta:

        model =  ExecutiveLunch

        fields = [
            'soup',
            'main_curse',
            'dessert',
            'juice',
            'date',
            'stock',
            'restaurant',
        ]