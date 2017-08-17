from django import forms
from catalogoapp.models.style import Style

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Style
        fields = [
            'color',
            'font',
            'size',
        ]
        labels = {
            'color': 'Color de letra del Restaurante',
            'font': 'Tipo de letra del Restaurante',
            'size': 'Tamaño de letra'
        }
        widgets = {
            'color': forms.Select(),
            'font': forms.Select(),
            'size': forms.Select(),
        }
