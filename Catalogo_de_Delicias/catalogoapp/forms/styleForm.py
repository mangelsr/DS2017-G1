from django import forms
from catalogoapp.models.style import Style

class StyleForm(forms.ModelForm):
    class Meta:
        model = Style
        fields = [
            'color',
            'font',
        ]
        labels = {
            'color': 'Color de letra del Restaurante',
            'font': 'Tipo de letra del Restaurante',
        }
        widgets = {
            'color': forms.Select(),
            'font': forms.Select(),
        }
