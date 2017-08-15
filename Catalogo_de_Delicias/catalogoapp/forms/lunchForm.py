from django import forms

from catalogoapp.models.lunch import Lunch


class LunchForm(forms.ModelForm):

    class Meta:
        model = Lunch
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
            'soup': forms.Select
                (attrs={'class': 'form-control', 'id': 'soup'}),
            'main_curse': forms.Select
                (attrs={'class': 'form-control', 'id': 'main_course'}),
            'date': forms.DateInput(),
        }