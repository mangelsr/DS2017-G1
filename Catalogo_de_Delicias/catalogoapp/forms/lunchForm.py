from django import forms
from django.forms.extras.widgets import SelectDateWidget

from catalogoapp.models.lunch import Lunch
from catalogoapp.models.dish import Dish


class LunchForm(forms.ModelForm):

    #dishes = Dish.objects.filter(dish_choice='Sopa')

    date = forms.DateField(widget = forms.SelectDateWidget(), label='Fecha del almuerzo')
    soup = forms.ModelChoiceField(queryset=Dish.objects.all(), label='Sopa del almuerzo')
    main_curse = forms.ModelChoiceField(queryset=Dish.objects.all(), label='Plato fuerte del almuerzo')

    class Meta:

        model = Lunch

        fields = [
            'soup',
            'main_curse',
            'date',
        ]