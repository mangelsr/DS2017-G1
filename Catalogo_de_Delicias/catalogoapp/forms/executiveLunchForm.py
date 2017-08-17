from django import forms

from catalogoapp.models.executiveLunch import ExecutiveLunch
from catalogoapp.models.dish import Dish


class ExecutiveLunchForm(forms.ModelForm):

    date = forms.DateField(widget = forms.SelectDateWidget(), label='Fecha del almuerzo')
    soup = forms.ModelChoiceField(queryset=Dish.objects.all(), label='Sopa del almuerzo')
    main_curse = forms.ModelChoiceField(queryset=Dish.objects.all(), label='Plato fuerte del almuerzo')
    juice = forms.ModelChoiceField(queryset=Dish.objects.all(), label='Jugo del postre')
    dessert = forms.ModelChoiceField(queryset=Dish.objects.all(),label='Postre del almuerzo')   

    class Meta:

        model =  ExecutiveLunch

        fields = [
            'soup',
            'main_curse',
            'dessert',
            'juice',
            'date',
        ]