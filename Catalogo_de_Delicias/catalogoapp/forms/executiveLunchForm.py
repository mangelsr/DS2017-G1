from django import forms
from catalogoapp.models.executiveLunch import ExecutiveLunch


class ExecutiveLunchForm(forms.ModelForm):

    class Meta:
        model =  ExecutiveLunch
        fields = [
            'soup',
            'main_curse',
            'date',
            'dessert',
            'juice',
        ]
        labels = {
            'soup': 'Sopa del almuerzo',
            'main_curse': 'Plato fuerte del almuerzo',
            'date': 'Fecha del almuerzo',
            'dessert': 'Postre del almuerzo',
            'juice': 'Jugo del postre',
        }
        widgets = {
            'soup': forms.Select(attrs={'class': 'form-control', 'id': 'soup'}),
            'main_curse': forms.Select(attrs={'class': 'form-control', 'id': 'main_course'}),
            'date': forms.DateInput(),
            'dessert': forms.Select(attrs={'class': 'form-control', 'id': 'dessert'}),
            'juice': forms.Select(attrs={'class': 'form-control', 'id': 'juice'}),
        }