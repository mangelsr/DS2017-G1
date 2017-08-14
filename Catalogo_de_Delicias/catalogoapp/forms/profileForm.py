from django import forms
from catalogoapp.models.profile import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'role',
            'restaurant',
        ]
        labels = {
            'role': 'Rol del usuario',
            'restaurant': 'Restaurante en que labora',
        }
        widgets = {
            'role': forms.Select(),
            'restaurant': forms.Select(),
        }
